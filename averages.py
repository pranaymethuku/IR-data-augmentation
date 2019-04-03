import json

data = ""

with open('accuracies.json', 'r') as file:
    data = file.read().replace('\n', '')

# remove all whitespace
data = "".join(data.split())

j = json.loads(data)

print('total average')
for k,v in j.items():
    avg = sum(v) / len(v)
    print("{}: {}".format(k, avg))

print('averages of second half:')

for k,v in j.items():
    avg = sum(v[5:]) / len(v[5:])
    print("{}: {}".format(k, avg))

print('weighted averages')
for k,v in j.items():
    avg = sum([(i + 1) * acc for i, acc in enumerate(v)]) / sum([i for i in range(1, 11)])
    print("{}: {}".format(k, avg))
