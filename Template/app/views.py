from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname'		: 'Lee'}
	posts = [
		{
			'author': {
				'nickname'	: 'John'
			},
			'body'	: 'Beautiful day in US'
		},
		{
			'author': {
				'nickname'	: 'Susan'
			},
			'body'	: 'The Aengers movie was so cool!'
		}
	]
	return render_template('index.html',
			title = 'Home',
			user = user,
			posts = posts
		)