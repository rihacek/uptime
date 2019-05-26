from app import app, models, config
from flask import render_template, redirect
import json

@app.route('/')
@app.route('/index')
def index():
    thisDash = models.Dashboard()
    return render_template('index.html', dashboard = thisDash)
    
@app.route('/hello')
def hello_stranger():
    return render_template('hello.html', name = 'stranger')

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)

@app.route('/ping')
@app.route('/ping/list')
def ping():
    return render_template('ping.html')

@app.route('/ping/list/<pw>')
def ping_list(pw):
    if pw == config.Secrets.pingsecret:
        thisList = models.PingList()
        return thisList.toJSON()
    else:
        return redirect('/ping')


