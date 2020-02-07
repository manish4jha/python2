import json

with open('sample.txt') as f:
  data = json.load(f)


print(data)
