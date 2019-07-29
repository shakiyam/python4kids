import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    a = random.randrange(1, 10)
    b = random.randrange(1, 10)
    return f'{a} * {b} = {a * b}'
