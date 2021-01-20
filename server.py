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
    over_view = request.form["over_view"]
    get_id = request.form["get_id"]
    x = requests.post(BLOG_URL, data={"over_view": over_view, "get_id": get_id})
    return x.content

if __name__ == '__main__':
    app.debug=True
    port = int(os.environ.get('PORT', 5000))
    app.run(threaded=True, port=port, host='0.0.0.0')
