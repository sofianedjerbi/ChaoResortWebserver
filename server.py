#!/usr/bin/env python
import os
import flask
import requests
from flask import render_template, request

# Create the application.
app = flask.Flask(__name__)
BLOG_URL = "http://nefault1s.online/Blog.php"

@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')

@app.route('/blog', methods=['POST'])
def news():
    print(request.data)
    print(request.text)
    #requests.post(BLOG_URL, data={})
    return render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    port = int(os.environ.get('PORT', 5000))
    app.run(threaded=True, port=port, host='0.0.0.0')
