# coding=utf-8
import json

jsonString = '[{"title":"Ahnkron, Sandra"},{"title":"Appelgren, Håkan"},{"title":"Atterbom Thomas"}]'
jsonData = json.loads(jsonString)
for entry in jsonData:
    print entry['title']
