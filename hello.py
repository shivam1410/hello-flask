from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'say Hello'

@app.route('/hola')
def hola():
    return 'Hola Amigo'

@app.route('/hello')
def hello():
    return 'hello bro'