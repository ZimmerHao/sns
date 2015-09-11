# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/hello')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')











