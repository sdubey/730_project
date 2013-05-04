#!/usr/bin/python
from bottle import route, run, template

#@route('/hello/:name')
#def index(name='World'):
#    return template('<b>Hello {{name}}</b>!', name=name)



def read(filename):
	with open(filename, 'r') as f:
		return f.read()

@route('/')
def index():
    return read('home.html')

@route('/trend')
def trend():
    return 'I am so stupid'


run(host='localhost', port=8080)
