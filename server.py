#!/usr/bin/env python
import flask
import requests

# Create the application.
app = flask.Flask(__name__)
BLOG_URL = "http://nefault1s.online/Blog.php"

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return # Empty

@app.route('/news', methods=['POST'])
def news():
    print(request.data)
    print(request.text)
    #requests.post(BLOG_URL, data={})
    return data

if __name__ == '__main__':
    APP.debug=True
    APP.run()
