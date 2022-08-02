#!/usr/bin/env python3
# @elasmo 2022
# 
# Hue bridge API experiments
# 1. Retrieve all available resources
#
# Resources:
# https://developers.meethue.com/develop/hue-entertainment/hue-entertainment-api/#a-new-api-and-sdk
# 
import requests
import json
import urllib3
urllib3.disable_warnings()

hueKey = ""
baseUrl = "https://"

resourceUrl = baseUrl + "/clip/v2/resource"
resourceHeaders = {"hue-application-hueKey": hueKey }
r = requests.get(resourceUrl, headers=resourceHeaders, verify=False)
if r.status_code == 200:
    res_json = json.loads(r.text)
    print("[+] " + resourceUrl);
    print(json.dumps(res_json, indent=4))
else:
    print("[+] " + resourceUrl + " Failed: " + str(r.status_code))
