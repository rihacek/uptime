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

@app.route('/responses/<this_id>', methods = ['GET', 'POST'])
def response(this_id):
    if request.method == 'GET':
        #show details for the response by id
        thisResponse = models.Response(this_id)
        return render_template('response.html', thisResponse = thisResponse)
    if request.method == 'POST':
        #create a new response for the system in the POST
        #password to post, systemid, statusid, calltime, and duration:
            pw = request.form['pw'] #== config.Secrets.pingsecret:
            system = this_id
            status = request.form['st']
            time = request.form['time']
            duration = request.form['dur']
            
            update_to_be    = "We're going to update System %s "%(system)
            update_to_be   += "with Status %s, "%(status)
            update_to_be   += "Time %s, "%(time)
            update_to_be   += "and Duration %sms."%(duration)

            return update_to_be
        
    else:        
        return abort(405) #other methods not allowed