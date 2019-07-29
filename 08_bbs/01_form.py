from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return render_template('01.html')
