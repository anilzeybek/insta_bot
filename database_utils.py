import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# c.execute("SELECT * FROM customers")
# print(c.fetchall())


def add_like(liker_account, liked_account, liked_post):
    x = (liker_account, liked_account, liked_post)
    c.execute("INSERT INTO likes (liker_account, liked_account, liked_post) VALUES (?, ?, ?)", x)
    conn.commit()


def add_follow_request(requester_account, requested_account):
    x = (requester_account, requested_account, 0, 0)
    c.execute("INSERT INTO follow_requests (requester_account, requested_account, accepted, declined) VALUES (?, ?, ?, ?)", x)
    conn.commit()


def add_blacklist(account):
    x = (account, 0)
    c.execute("INSERT INTO blacklist (account, request_declined) VALUES (?, ?)", x)
    conn.commit()


def add_blocker(blocker_account, blocked_account):
    x = (blocker_account, blocked_account)
    c.execute("INSERT INTO blockers VALUES (?, ?)", x)
    conn.commit()


def close_conn():
    conn.close()
