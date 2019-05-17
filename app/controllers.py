from app import app
from flask import render_template
from app import data #maybe look at refactoring this out later 2019-05-15
from app import models

@app.route('/')
@app.route('/index')
def index():
    thisDash = models.Dashboard()
    return render_template('index.html', dashboard = thisDash)
    #create new dashboard object
    #call db and assign dashboard model's systems array to 
    
@app.route('/hello')
def hello_stranger():
    #return render_template('hello.html', name = MyClass.stranger)
    __sysdao = data.SystemDAO()
    return render_template('hello.html', name = __sysdao.getSystems())
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)
