#!/usr/bin/env python3
# @elasmo 2022
# 
# Hue bridge API experiments
# Retrieve entertainment area configuraiton
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

entertainmentConfigUrl = baseUrl + "/clip/v2/resource/entertainment_configuration"
entertainmentHeaders = {"hue-application-hueKey": hueKey }
r = requests.get(entertainmentConfigUrl, headers=entertainmentHeaders, verify=False)
res_json = json.loads(r.text)
print(json.dumps(res_json, indent=4))
