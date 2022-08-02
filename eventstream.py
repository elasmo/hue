#!/usr/bin/env python3
# @elasmo 2022
# 
# Hue bridge API experiments
# Open eventsteram to listen to updates
#
# Resources:
# https://developers.meethue.com/develop/hue-entertainment/hue-entertainment-api/#a-new-api-and-sdk
# 
import requests
import json
import urllib3
import string
urllib3.disable_warnings()

hueKey = ""
baseUrl = "https://"

streamUrl = baseUrl + "/eventstream/clip/v2"
streamHeaders = {"Accept": "text/event-stream", "hue-application-hueKey": hueKey }
eventstream = requests.get(stream, headers=streamHeaders, verify=False, timeout=20000, stream=True)
for events in eventstream.iter_lines():
    try:
        events = json.loads(event[6:].decode('utf-8'))
        for event in events:
            print(json.dumps(event['data'], indent=4))
    except:
        pass
