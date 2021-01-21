import requests
import psycopg2
import os
import time
""" CONFIG : News
 *
CREATE TABLE public.announcements (
	id SMALLINT PRIMARY KEY,
	title VARCHAR (50) UNIQUE NOT NULL,
	news VARCHAR (512) NOT NULL
 );
 INSERT INTO public.announcements
 VALUES (id, title, news);
 DATE FORMAT : [Aug-06-17]
 (Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec)
"""
DATABASE_URL = os.environ['DATABASE_URL']
BLOG_URL = "http://nefault1s.online/Blog.php"
con = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = con.cursor()
mod_news = {
    11: ("Thank you for downloading this mod![Jan-20-21]", "Hello! I hope you're having fun! Chao Resort Island isn't dead yet, we're working hard on this mod. A new unlockable character is coming soon. Click to join the mod discord![https://discord.gg/hycdkQAUKN")
}

x = requests.post(BLOG_URL, data={"over_view": 1, "get_id": 0})

news = []

titles = [e + ']' for e in x.text.split(']')]
titles.pop()
titles.reverse() # It's ugly but whatever.

for i in range(len(titles)):
    x = requests.post(BLOG_URL, data={"over_view": 0, "get_id": i+1})
    news.append(x.text)

for id in mod_news:
    titles.insert(id, mod_news[id][0])
    news.insert(id, mod_news[id][1])

for i in range(len(news)): # Escape quotes
    news[i] = news[i].replace("'", "''")

for i in range(len(titles)):
    txt = f"INSERT INTO \"public\".\"announcements\" (\"id\", \"title\", \"news\")  VALUES ({i+1}, '{titles[i]}', '{news[i]}');"
    cur.execute(f"SELECT * FROM public.announcements WHERE id={i+1};")
    raw_data = cur.fetchall()
    if len(raw_data) == 0:
        cur.execute(txt)

con.commit()
con.close()
# DONE !
