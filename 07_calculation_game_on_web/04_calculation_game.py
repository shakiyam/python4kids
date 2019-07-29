import random

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def question():
    a = random.randrange(1, 10)
    b = random.randrange(1, 10)
    return render_template('04_question.html', a=a, b=b)


@app.route('/', methods=['POST'])
def answer():
    a = int(request.form['a'])
    b = int(request.form['b'])
    answer = request.form['answer']
    if answer.isdigit() and int(answer) == a * b:
        message = 'Good job!'
    else:
        message = 'Oops!'
    return render_template(
        '04_answer.html', a=a, b=b, answer=answer, message=message)
