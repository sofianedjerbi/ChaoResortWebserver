#!/usr/bin/env python
import flask
import requests

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
    app.run(threaded=True, port=5000, host='0.0.0.0')
