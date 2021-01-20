import requests
import psycopg2
from os import environ
""" CONFIG : News
 *
CREATE TABLE accounts (
	id SMALLINT PRIMARY KEY,
	title VARCHAR (50) UNIQUE NOT NULL,
	news VARCHAR (512) NOT NULL
 );
 INSERT INTO News
 VALUES (id, title, news);
 DATE FORMAT : [Aug-06-17]
 (Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec)
"""
DATABASE_URL = os.environ['DATABASE_URL']
BLOG_URL = "http://nefault1s.online/Blog.php"
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
mod_news = {
    11: ("Thanks for downloading this mod![Jan-20-21]", "I hope you'll like it! Chao Resort Island isn't dead yet! We're working on a new character! Click to join the mod discord![https://discord.gg/hycdkQAUKN")
}

x = requests.post(BLOG_URL, data={"over_view": 1, "get_id": 0})

news = []

titles = [e + ']' for e in x.content.split(']')]
titles.pop()
titles.reverse() # It's ugly but whatever.

for i in range(len(titles)):
    news.append(requests.post(BLOG_URL, data={"over_view": 0, "get_id": i+1}))

for i in mod_news:
    titles.insert(i, mod_news[i][0])
    news.insert(i, mod_news[i][1])

for i in range(len(titles)):
    cur.execute(f"INSERT INTO News VALUES ({i+1}, {titles[i]}, {news[i]});")

con.close()
# DONE !
