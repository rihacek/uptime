from app import app, models, config
from flask import render_template, redirect, request, abort
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

@app.route('/responses/<response_id>', methods = ['GET', 'POST', 'DELETE'])
def response(response_id):
    if request.method == 'GET':
        #do response id things
        thisResponse = models.Response(response_id)
        return render_template('response.html', thisResponse = thisResponse)
    if request.method == 'POST':
        #do write things
        return redirect('/ping') #placeholder
    if request.method == 'DELETE':
        #remove this response
        return redirect('/ping') #placeholder
    else:        
        return abort(405) #method not allowed