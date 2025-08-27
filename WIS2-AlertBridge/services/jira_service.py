import requests
import logging

def ticket_is_closed(issue_key, jira_url, jira_token):
    try:
        url = f"{jira_url}/{issue_key}"
        headers = {"Authorization": f"Bearer {jira_token}", "Content-Type": "application/json"}
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code != 200:
            logging.warning(f"Ticket verification {issue_key} failed (HTTP {response.status_code})")
            return False
        statut = response.json()['fields']['status']['name'].lower()
        return statut in ['done', 'closed', 'resolved']
    except Exception as e:
        logging.error(f"Error: ticket_is_closed({issue_key}): {e}")
        return False

def add_watcher_to_ticket(issue_key, watcher_id, jira_url, jira_token):
    url = f"{jira_url}/{issue_key}/watchers"
    headers = {"Authorization": f"Bearer {jira_token}", "Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, json=watcher_id, verify=False)
        if response.status_code == 204:
            logging.info(f"Watcher {watcher_id} added to ticket {issue_key}")
            return True
        else:
            logging.warning(f"Failed to add watcher: {response.status_code} {response.text}")
            return False
    except Exception as e:
        logging.error(f"Error add_watcher_to_ticket: {e}")
        return False

def create_jira_ticket(summary, description, centre_id, jira_url, jira_token, assignee, watcher):
    payload = {
        "fields": {
            "project": {"key": "TESTWIS"},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Incident"}
        }
    }
    if assignee:
        payload["fields"]["assignee"] = {"name": assignee}
    headers = {"Authorization": f"Bearer {jira_token}", "Content-Type": "application/json"}

    try:
        response = requests.post(jira_url, headers=headers, json=payload, verify=False)
        if response.status_code == 201:
            ticket_key = response.json()['key']
            logging.info(f"Jira ticket created: {ticket_key} (Assigned to {assignee})")
            add_watcher_to_ticket(ticket_key, watcher["accountId"], jira_url, jira_token)
            return ticket_key
        else:
            logging.error(f"Failed to create Jira ticket: {response.status_code} {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error create_jira_ticket: {e}")
        return None
