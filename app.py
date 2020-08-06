# main python file
from flask import Flask
# from parser import parse
from parser_driver import parse

app = Flask(__name__)

@app.route('/parse')
def start():
    parse()
    return 'Done!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)