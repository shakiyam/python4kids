from datetime import datetime
from datetime import timezone

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

app = Flask(__name__)
posts = []


@app.route('/', methods=['GET'])
def get():
    return render_template('04.html', posts=posts)


@app.route('/', methods=['POST'])
def post():
    posts.insert(0, {
        'message': request.form['message'],
        'created_at': datetime.now(timezone.utc)
    })
    return redirect('/', 303)
