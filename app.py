# main python file
from flask import Flask
from parser_driver import parse
import requests
import json

app = Flask(__name__)


@app.route('/parse')
def start():
    data = parse()

    url = 'http://78.155.206.12/items'
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 201:
        return {'message': 'Success!'}
    return {'message': 'An error has occurred.'}


if __name__ == '__main__':
    app.run(port=5000, debug=True)
