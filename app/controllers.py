from app import app
from flask import render_template
from app.models import MyClass
from app import data

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/hello')
def hello_stranger():
    #return render_template('hello.html', name = MyClass.stranger)
    __sysdao = data.SystemDAO()
    return render_template('hello.html', name = __sysdao.getSystems())
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)
