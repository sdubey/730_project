#!/usr/bin/python
from bottle import route, run, template, post, request

#@route('/hello/:name')
#def index(name='World'):
#    return template('<b>Hello {{name}}</b>!', name=name)


def read(filename):
	with open(filename, 'r') as f:
		return f.read()

@route('/')
def index():
    return read('home.html')


@post('/trend') # or @route('/trend', method='POST')
def trend():
    date     = request.forms.get('date')
    input_file = 'data/%s.txt' %(date)
    return read(input_file)


run(host='localhost', port=8080)
