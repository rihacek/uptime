from app import app, models, config, data
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

@app.route('/responses/<this_id>', methods = ['GET', 'POST'])
def response(this_id):
    if request.method == 'GET':
        #show details for the response by id
        thisResponse = models.Response(this_id)
        return render_template('response.html', thisResponse = thisResponse)
    if request.method == 'POST':
        #make sure that not just anyone is posting:
        if request.form['pw'] == config.Secrets.pingsecret:
            #capture details for this response record    
            system = this_id
            status = request.form['st']
            time = request.form['time']
            duration = request.form['dur']            
            
            x = data.ResponseDAO()
            newID = x.logResponse(system, status, time, duration)
            return newID
        else:
            return "no good"        
    else:        
        return abort(405) #other methods not allowed