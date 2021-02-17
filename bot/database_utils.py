import sqlite3
import logging


logging.basicConfig(filename='../logfile.log', level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
conn = sqlite3.connect('../database.db')
c = conn.cursor()


def add_like(liker_account, liked_account):
    x = (liker_account, liked_account)
    c.execute("INSERT INTO likes (liker_account, liked_account) VALUES (?, ?)", x)
    conn.commit()

    logging.warning(f"{liker_account} liked {liked_account}'s post")


def add_follow_request(requester_account, requested_account):
    x = (requester_account, requested_account, 0, 0)
    c.execute("""INSERT INTO follow_requests (requester_account, requested_account, accepted, declined) 
    VALUES (?, ?, ?, ?)""", x)
    conn.commit()

    logging.warning(f"{requester_account} send follow request to {requested_account}")


def add_dm(sender_account, sent_account, message):
    x = (sender_account, sent_account, message)
    c.execute("INSERT INTO dm (sender_account, sent_account, message) VALUES (?, ?, ?)", x)
    conn.commit()

    logging.warning(f"{sender_account} send dm to {sent_account}")


def find_follow_requests(requester_account, days):
    usernames = []

    c.execute(
        f"SELECT requested_account FROM follow_requests WHERE requester_account = ? AND request_date < datetime('now', '-{days} days')",
        (requester_account,))
    rows = c.fetchall()

    for row in rows:
        usernames.append(row[0])

    return usernames


def delete_follow_request(requester_account, requested_account):
    x = (requester_account, requested_account)
    c.execute("DELETE FROM follow_requests WHERE requester_account = ? AND requested_account = ?", x)
    conn.commit()


def add_blacklist(account):
    x = (account, 0)
    c.execute("INSERT INTO blacklist (account, request_declined) VALUES (?, ?)", x)
    conn.commit()

    logging.warning(f"{account} has been added to blacklist")


def in_blacklist(account):
    c.execute("SELECT * FROM blacklist WHERE account = ?", (account,))
    if c.fetchone():
        logging.warning(f"{account} is in blacklist, so skipping\n")
        return True

    return False


def close_conn():
    conn.close()
