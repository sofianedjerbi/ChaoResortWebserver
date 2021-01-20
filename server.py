import os
import flask
import psycopg2
from flask import render_template, request

# Create the application.
app = flask.Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL']
BLOG_URL = "http://nefault1s.online/Blog.php"
conn = psycopg2.connect(DATABASE_URL)
CUR = conn.cursor()

class New:
    def __init__(title, id):
        self.title = title
        self.id = id

@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')

@app.route('/blog', methods=['POST'])
def news():
    over_view = request.form["over_view"]
    get_id = request.form["get_id"]
    CUR.execute("SELECT * ... FROM table_name WHERE condition;")

    if over_view == 0:
        txt.append(mod_news)
    return txt

if __name__ == '__main__':
    app.debug=True
    port = int(os.environ.get('PORT', 5000))
    app.run(threaded=True, port=port, host='0.0.0.0')
