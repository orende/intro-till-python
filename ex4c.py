# coding=utf-8
import json, requests

requestData = requests.get('http://httpbin.org/get').text
jsonData = json.loads(requestData)
for key, value in jsonData.iteritems():
    print key, value
