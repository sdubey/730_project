#!/usr/bin/python
from trend import trend
from bottle import route, run, template, post, request

def read(filename):
	with open(filename, 'r') as f:
		return f.read()

@route('/')
def index():
    return read('home.html')

@route('/lib/d3.js')
def index():
    return read('lib/d3.js')

@route('/lib/d3.layout.cloud.js')
def index():
    return read('lib/d3.layout.cloud.js')

@route('/css/style.css')
def index():
    return read('css/style.css')

@post('/trend') # or @route('/trend', method='POST')
def run_trend():
    date     = request.forms.get('date')
    output_file = 'data/%s.html' %(date)
    return read(output_file)

run(host='localhost', port=8080)
