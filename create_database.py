import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE likes (
        liker_account TEXT,
        liked_account TEXT,
        liked_post TEXT,
        like_date DATE DEFAULT (datetime('now','localtime'))
    )
""")

c.execute("""
    CREATE TABLE follow_requests (
        requester_account TEXT,
        requested_account TEXT,
        accepted INTEGER,
        declined INTEGER,
        request_date DATE DEFAULT (datetime('now','localtime'))
    )
""")

c.execute("""
    CREATE TABLE blacklist (
        account TEXT,
        request_declined INTEGER,
        blacklist_date DATE DEFAULT (datetime('now','localtime'))
    )
""")

c.execute("""
    CREATE TABLE blockers (
        blocker_account TEXT,
        blocked_account TEXT
    )
""")


conn.commit()
conn.close()
