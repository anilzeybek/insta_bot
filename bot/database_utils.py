import sqlite3

conn = sqlite3.connect('../database.db')
c = conn.cursor()


def add_like(liker_account, liked_account):
    x = (liker_account, liked_account)
    c.execute("INSERT INTO likes (liker_account, liked_account) VALUES (?, ?)", x)
    conn.commit()

    print(f"{liker_account} liked {liked_account}'s post")


def add_follow_request(requester_account, requested_account):
    x = (requester_account, requested_account, 0, 0)
    c.execute("""INSERT INTO follow_requests (requester_account, requested_account, accepted, declined) 
    VALUES (?, ?, ?, ?)""", x)
    conn.commit()

    print(f"{requester_account} send follow request to {requested_account}")


def add_blacklist(account):
    x = (account, 0)
    c.execute("INSERT INTO blacklist (account, request_declined) VALUES (?, ?)", x)
    conn.commit()

    print(f"{account} has been added to blacklist")
    print("--------------\n")


def add_blocker(blocker_account, blocked_account):
    x = (blocker_account, blocked_account)
    c.execute("INSERT INTO blockers VALUES (?, ?)", x)
    conn.commit()

    print(f"{blocker_account} blocked {blocked_account}")


def in_blacklist(account):
    c.execute("SELECT * FROM blacklist WHERE account = ?", (account,))
    if c.fetchone():
        print(f"{account} is in blacklist, so skipping\n")
        return True

    return False


def close_conn():
    conn.close()
