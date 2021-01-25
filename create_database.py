import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE likes (
        liker_account TEXT,
        liked_account TEXT,
        liked_post TEXT,
        like_date TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

c.execute("""
    CREATE TABLE follow_requests (
        requester_account TEXT,
        requested_account TEXT,
        request_date TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

c.execute("""
    CREATE TABLE blacklist (
        account TEXT,
        request_declined INTEGER,
        blacklist_date TEXT DEFAULT CURRENT_TIMESTAMP
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
