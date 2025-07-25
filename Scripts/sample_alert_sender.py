import requests
import json

THEHIVE_URL = 'http://192.168.0.103:9000/api/case'
API_KEY = 'Your_TheHive_API_Key'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

alert_case = {
    "title": "Wazuh Alert - Netstat Status Changed",
    "description": "Alert from Wazuh: Listened ports status changed.",
    "severity": 2,
    "tags": ["wazuh", "automation"],
    "tlp": 2,
    "pap": 2
}

response = requests.post(THEHIVE_URL, headers=headers, data=json.dumps(alert_case))
print(response.status_code, response.text)
