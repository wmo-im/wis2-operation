import json
import uuid
import logging
import paho.mqtt.publish as publish

def publish_mqtt_notification(alertname, severity, summary, starts_at, broker, port, username, password):
    try:
        topic = "monitor/a/wis2/ma-marocmeteo-global-monitor"
        payload = {
            "specversion": "1.0",
            "type": "int.wmo.codes.performance",
            "source": "ma-marocmeteo-global-monitor",
            "subject": alertname,
            "id": str(uuid.uuid4()),
            "time": starts_at,
            "datacontenttype": "application/json",
            "dataschema": "int.wmo.codes.event.data.v1",
            "data": {"level": severity, "text": summary}
        }
        publish.single(
            topic,
            payload=json.dumps(payload),
            hostname=broker,
            port=port,
            auth={"username": username, "password": password}
        )
        logging.info(f"MQTT notification published")
        return True
    except Exception as e:
        logging.error(f"MQTT send error: {e}")
        return False
