#!/usr/bin/python3
"""A script to get the id of a datadog dashboard"""
import os
import requests
import json

# Read API key and app key from environment variables
api_key = os.environ.get('DD_API_KEY')
datadog_app_key = os.environ.get('DD_APP_KEY')

if not api_key or not datadog_app_key:
    print("Please set both DD_API_KEY and DD_APP_KEY environment variables.")
    exit(1)

url = 'https://api.datadoghq.com/api/v1/dashboard'
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': datadog_app_key,
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    dashboards = response.json()
    target_dashboard_title = 'First_dashboard'
    for dashboard in dashboards['dashboards']:
        if dashboard['title'] == target_dashboard_title:
            dashboard_id = dashboard['id']
            print(f"Dashboard ID for '{target_dashboard_title}': {dashboard_id}")
            break
    else:
        print(f"Dashboard '{target_dashboard_title}' not found.")
else:
    print(f"Error: {response.status_code} - {response.text}")
