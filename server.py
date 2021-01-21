import os
import flask
import psycopg2
from flask import render_template, request

# Create the application.
app = flask.Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL']
BLOG_URL = "http://nefault1s.online/Blog.php"
con = psycopg2.connect(DATABASE_URL, sslmode='require')
CUR = con.cursor()

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
    #print(f"over:{over_view}; id:{get_id}")
    if over_view == "1":
        titles = ""
        CUR.execute("SELECT count(*) FROM public.announcements;") # Get cardinal
        raw_count = CUR.fetchall()
        card = raw_count[0][0]
        #print(f"card:{card}")
        for i in range(1, card+1):
            CUR.execute(f"SELECT * FROM public.announcements WHERE id={i};")
            raw_data = CUR.fetchall()
            #print(f"raw:{raw_data}; titles:{titles}")
            titles += raw_data[0][1]
        return titles # Title list
    else:
        CUR.execute(f"SELECT * FROM public.announcements WHERE id={get_id};")
        raw_data = CUR.fetchall()
        msg = raw_data[0][2]
        return msg

if __name__ == '__main__':
    app.debug=True
    port = int(os.environ.get('PORT', 5000))
    app.run(threaded=True, port=port, host='0.0.0.0')
