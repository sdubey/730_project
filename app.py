#!/usr/bin/python
from trend import trend
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
def run_trend():
    date     = request.forms.get('date')
    input_file = 'data/%s.txt' %(date)
    output_dir = '/tmp/%s' %(date)
    trend.trend(input_file, output_dir)

    output_file = '%s/part-00000' %(output_dir)
    return read(output_file)


run(host='localhost', port=8080)
