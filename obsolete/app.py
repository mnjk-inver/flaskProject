from flask import Flask
from testing import helloworld

app = Flask(__name__)

@app.route('/')
def samplefunction():
    return "hello world"

@app.route('/test')
def test():
    x = helloworld()
    return x
