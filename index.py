import requests
import json
import os
import re
import time
url_make_webhooks =None

indexer = True

while indexer:
    try:
        if url_make_webhooks is None:
            user_key = input('Enter your url make webhooks token: ').strip()
        else:
            user_key = url_make_webhooks

        if not re.match(r'https://', user_key):
            raise ValueError("Invalid URL. It must start with http:// or https://")
        

        url_make_webhooks = user_key
        print('Client initialized successfully. Token is valid.')

        indexer = False
    except Exception as e:
        print("Details:", e)
        url_make_webhooks = None

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, "results_test.json"), "r", encoding="utf-8") as file:
    data = json.load(file)

def clean_item(item):
    return {k: (v if v is not None else "") for k, v in item.items()}

for i, item in enumerate(data, start=1):
    clean_data = clean_item(item)
    try:
        response = requests.post(
            url_make_webhooks,
            json=clean_data,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code in [200, 202]:
            print(f"{i}: ✅ Successfully sent '{item.get('name','(no name)')}'")
        else:
            print(f"{i}: ❌ Error {response.status_code} sending '{item.get('name','(no name)')}'")
    except Exception as e:
        print(f"{i}: ⚠ Exception sending '{item.get('name','(no name)')}': {e}")
    time.sleep(0.5)

print(f"\nTotal items sent: {len(data)}")
