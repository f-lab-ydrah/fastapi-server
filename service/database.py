import sqlite3

conn = sqlite3.connect("posts.db")

cur = conn.cursor()

cur.execute("""
            CREATE TABLE posts (
                post_id integer primary key autoincrement,
                author text,
                title text,
                content text,
                created_at sysdate
                )
            """)

rows = cur.fetchall()

for row in rows:
    print(row)
    
conn.close()