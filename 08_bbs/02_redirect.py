from flask import Flask
from flask import redirect
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return render_template('02.html')


@app.route('/', methods=['POST'])
def post():
    return redirect('/', 303)
