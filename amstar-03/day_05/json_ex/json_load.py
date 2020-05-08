import json

# Opening a file with context manager
with open('sample.txt') as f:
  data = json.load(f)


print(data)

for key in data.keys():
    print(key, ' -----> ', data[key])
    print("-"*30)
    for element in data[key]:
        print("-"*30)
        for elementkey in element.keys():
            print('{0:15}  ---->  {1:15}'.format(elementkey, element[elementkey]))
            #print(elementkey, element[elementkey])
        print("-"*30)
