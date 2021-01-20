import requests
import mariadb
""" CONFIG : News
 *
 * CREATE TABLE News (
 * id SMALLINT UNSIGNED PRIMARY KEY,
 * title VARCHAR(32) NOT NULL,
 * news VARCHAR(512) NOT NULL
 * )
 INSERT INTO News
 VALUES (id, title, news);
"""
BLOG_URL = "http://nefault1s.online/Blog.php"
conn = mariadb.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=DATABASE
    )
cur = conn.cursor()
mod_news = {}

x = requests.post(BLOG_URL, data={"over_view": 1, "get_id": 0})
titles = [e + ']' for e in x.content.split(']')]
titles.pop()
titles.reverse() # It's ugly but whatever.
for i in range(0, len(titles)):
    txt = requests.post(BLOG_URL, data={"over_view": 1, "get_id": i+1})
    cur.execute(f"INSERT INTO News VALUES ({i+1}, {titles[i]}, {txt});")

# DONE !
