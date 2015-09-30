from flask import Flask
from flask import render_template
import json
from pprint import pprint

def get_data():
    with open('data.json') as data_file:
        return json.load(data_file)

def increment_data(knockouts=False, kills=False):
    data = get_data()
    with open('data.json', 'w') as out_file:
        if knockouts:
            data['knockouts'] = data['knockouts'] + 1
        if kills:
            data['kills'] = data['kills'] + 1
        json.dump(data, out_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', **get_data())

@app.route('/kill', methods=['POST'])
def kill():
    print "kill"
    increment_data(kills=True)
    return render_template('index.html', message='Nice job!', **get_data())

@app.route('/knockout', methods=['POST'])
def ko():
    print "ko"
    increment_data(knockouts=True)
    return render_template('index.html', message='Sweet!', **get_data())

if __name__ == '__main__':
    app.run()
