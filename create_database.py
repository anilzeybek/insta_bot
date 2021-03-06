import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS likes (
        liker_account TEXT,
        liked_account TEXT,
        like_date DATE DEFAULT (datetime('now','localtime'))
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS follow_requests (
        requester_account TEXT,
        requested_account TEXT,
        accepted INTEGER,
        declined INTEGER,
        request_date DATE DEFAULT (datetime('now','localtime'))
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS dm (
        sender_account TEXT,
        sent_account TEXT,
        message TEXT,
        dm_date DATE DEFAULT (datetime('now','localtime'))
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS blacklist (
        account TEXT,
        request_declined INTEGER,
        blacklist_date DATE DEFAULT (datetime('now','localtime'))
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        account TEXT UNIQUE
    )
""")

conn.commit()
conn.close()
