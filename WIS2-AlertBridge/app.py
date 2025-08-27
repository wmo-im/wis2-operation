from flask import Flask, request, jsonify
import configparser
import logging

from utils.logger import setup_logger
from services.redis_service import get_redis_client
from services.assignee_service import load_assignees_from_csv, get_current_assignee, get_assignee_from_centre
from services.jira_service import create_jira_ticket, ticket_is_closed
from services.mqtt_service import publish_mqtt_notification

# Flask app
app = Flask(__name__)
logger = setup_logger()

# Config
config = configparser.ConfigParser()
config.read('config/access.ini')

JIRA_API_URL = config['JIRA']['url'].rstrip('/')
JIRA_AUTH_TOKEN = config['JIRA']['token']

MQTT_BROKER = config['MQTT']['broker']
MQTT_PORT = int(config['MQTT']['port'])
MQTT_USERNAME = config['MQTT']['username']
MQTT_PASSWORD = config['MQTT']['password']

# Redis
redis_client = get_redis_client()

# Load CSV
load_assignees_from_csv()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        for alert in data.get('alerts', []):
            labels = alert.get('labels', {})
            alertname = labels.get('alertname')
            severity = labels.get('severity')
            status = alert.get('status')
            starts_at = alert.get('startsAt')
            centre_id = labels.get('centre_id') or labels.get('report_by') or "unknown"
            summary = f"{centre_id} : {alert.get('annotations', {}).get('summary', '')}"
            alert_key = f"{alertname}:{centre_id}"

            if not all([alertname, severity, starts_at, status]):
                logger.error(f"Champs manquants : {alert}")
                continue

            if severity == "critical":
                description = f"{summary}\n\nAlert triggered at: {starts_at}\n\nReported By: ma-marocmeteo-global-monitor"
                ticket_id = redis_client.get(alert_key)
                if ticket_id:
                    ticket_id = ticket_id.decode()
                    if ticket_is_closed(ticket_id, JIRA_API_URL, JIRA_AUTH_TOKEN):
                        new_ticket = create_jira_ticket(summary, description, centre_id, JIRA_API_URL, JIRA_AUTH_TOKEN, get_assignee_from_centre(centre_id), get_current_assignee())
                        if new_ticket:
                            redis_client.set(alert_key, new_ticket)
                    else:
                        logger.info(f"Ticket already opened : {ticket_id}")
                else:
                    new_ticket = create_jira_ticket(summary, description, centre_id, JIRA_API_URL, JIRA_AUTH_TOKEN, get_assignee_from_centre(centre_id), get_current_assignee())
                    if new_ticket:
                        redis_client.set(alert_key, new_ticket)
            # else:
                # publish_mqtt_notification(alertname, severity, summary, starts_at, MQTT_BROKER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD)

        return jsonify({"status": "success"})
    except Exception as e:
        logger.error(f"Erreur webhook: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
