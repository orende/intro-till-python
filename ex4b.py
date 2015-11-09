# coding=utf-8
import json

with open('data.json', 'r') as myFile:
    jsonData = json.load(myFile)
    for entry in jsonData:
        print entry['title']
