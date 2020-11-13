from flask import Flask, request, Response
from datetime import datetime
import time

app = Flask(__name__)

messages= [
    {'name': 'Jack', 'time':  time.time(), 'text': 'Hi!'},
    {'name': 'Mary', 'time': time.time(), 'text': 'Hey!'},
    {'name': 'Nick', 'time': time.time(), 'text': 'Hi there!'},
]

@app.route("/send", methods=['POST'])
def send():
    name = request.json.get('name')
    text = request.json.get('text')
    if not name or isinstance(name, str) or \
            not text or isinstance(text, str):
        return Response(status=400)

    message = {'name': name, 'time': time.time(), 'text': text}
    messages.append(message)
    print(messages)
    return Response(status=200)

def filter_by_key(elements, key, threshold):
    filtered_elements = []

    for element in elements:
        if element[key] > threshold:
            filtered_elements.append(element)
    return filtered_elements

@app.route("/messages")
def messages_view():
    try:
        after = float(request.args['after'])
    except:
        return Response(status=400)
    filtered = filter_by_key(messages, key='time', threshold=after)
    return {'messages': filtered }

@app.route("/")
def hello():
    return "Hello, World! \
            <a href='/status'>Статус</a> \
            <a href='/messages?after=1598354226.697279'>Сообщения</a>"

def number_users(message_list):
    names = []
    for message in message_list:
        names.append(message['name'])
    return len(set(names))

@app.route("/status")
def status():
    return {
        'status': True,
        'name'  : 'Cool Messenger',
        'time'  : datetime.now(),
        'time1' : time.asctime(),
        'time2' : time.time(),
        'time3' : datetime.now().strftime('%H:%M:%S %d/%m/%Y'),
        'users' : number_users(messages),
        'messages':len(messages)
    }

app.run()