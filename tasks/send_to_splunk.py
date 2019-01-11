#!/usr/bin/env python

import sys
import json
import requests

params = json.load(sys.stdin)

print('params: ***')
print(json.dumps(params))
print('data: ***')
print(json.dumps(params['data']))

target = params['_target']

splunk_endpoint = target['uri']
splunk_token = target['token']

data = params['data']

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Splunk ' + splunk_token
}

response = requests.post(
    splunk_endpoint, headers=headers, json=data, verify=False)

result = {}
result['_output'] = response.text

print(json.dumps(result))
