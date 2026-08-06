# 🚨 WIS2 Alert → Jira Bridge  

A **Flask-based service** that receives alerts (via Prometheus/Alertmanager webhook) and automatically creates **Jira tickets**, with assignment, watchers, and rotation logic.  

## ✨ Features

- 📡 **Webhook endpoint** (`/webhook`) to receive Prometheus alerts.  
- 📝 Automatic creation of **Jira incidents** (`issuetype: Incident`).  
- 👥 Dynamic ticket assignment through:
  - **CSV mapping ISO2 → accountId** (`config/assignees.csv`)  
  - **Bi-weekly rotation** of watchers (15-day cycle).  
- 💾 **Redis persistence** to prevent duplicate ticket creation.  
- ✅ Checks ticket status (open/closed) before creating new ones.  

## 📊 Workflow

Prometheus/Alertmanager sends an alert to /webhook.

The service checks Redis for an existing ticket.

If none → creates a new Jira ticket with assignee & watcher.

If exists but ticket is closed → creates a new one.

Redis is updated with the new ticket reference.


