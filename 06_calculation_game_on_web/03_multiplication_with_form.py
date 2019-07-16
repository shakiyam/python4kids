import random

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    a = random.randrange(1, 10)
    b = random.randrange(1, 10)
    return render_template('03.html', a=a, b=b)
