from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/cat')
def cat():
    return 'Miauw!'


@app.route('/succes')
def succes():
    return 'Succes!'
