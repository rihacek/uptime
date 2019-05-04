from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)