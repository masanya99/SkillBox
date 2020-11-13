messages = [
    {'name': 'Jack', 'time': 1978238971, 'text': 'Hi!'},
    {'name': 'Mary', 'time': 2938742823, 'text': 'Hey!'},
    {'name': 'Nick', 'time': 5897423792, 'text': 'Hi there!'},
    {'name': 'Nick', 'time': 5897423753, 'text': 'Hi there!'}
]

# print(utils.max_by_key(messages, 'time'))
# print(utils.max_by_key([], 'time'))
#
# print(utils.filter_by_key(messages, 'time', 1978238971))
# print(utils.filter_by_key(messages, 'time', 2938742823))

names = []
for message in messages:
    names.append(message['name'])
print(len(set(names)))