# _*_ coding: utf-8 _*_
"""
model:
	Flask
	request
	make_response
	Flask-Script -> 命令行解析
		Manager类
"""
from flask import Flask, request, make_response
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
	# 一个上下文的例子(request)
	# user_agent = request.headers.get('User_Agent')
	# return '<p>Your browers is %s!</p>' % user_agent
	response = make_response('<h1>This documents carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return '<h1>Hello, World!</h1>', 200

@app.route('/user/<id>')
def user(id):
	return '<1>Hello, %s!</h1>' % id

if __name__ == '__main__':
	# app.run(debug=True)
	# 命令行方式输入参数 runserver --help
	manager.run()