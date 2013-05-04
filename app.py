#!/usr/bin/python
from bottle import route, run, template

#@route('/hello/:name')
#def index(name='World'):
#    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
def index():
    return 'Hello World'

run(host='localhost', port=8080)