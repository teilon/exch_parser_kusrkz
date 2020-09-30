# main python file
from flask import Flask
from parser_driver import parse
import requests
import json

from params import MANAGER_HOST

app = Flask(__name__)


@app.route('/parse')
def start():
    data = parse()

    url = 'http://{}/items'.format(MANAGER_HOST)
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return {'message': 'Success!'}
    return {'message': 'An error has occurred.'}


if __name__ == '__main__':
    app.run(port=5000, debug=True)
