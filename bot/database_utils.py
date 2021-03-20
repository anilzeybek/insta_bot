import psycopg2
import logging
import uuid


class DatabaseUtils:
    def __init__(self, client_id, local=False):
        logging.basicConfig(filename='../logfile.log', level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
        if local:
            self.conn = psycopg2.connect(dbname="instabot", user="postgres", host="localhost", password="postgres")
        else:
            self.conn = psycopg2.connect(dbname="instabot", user="postgres", host="localhost", password="postgres")
        self.c = self.conn.cursor()

        logging.warning(self.conn)

        self.UUID = str(uuid.uuid4())
        self.client_id = client_id

    def add_like(self, liker_account, liked_account):
        self.c.execute(f"INSERT INTO likes (liker_account, liked_account, client_id) VALUES ('{liker_account}', '{liked_account}', '{self.client_id}');")
        self.conn.commit()

        self.upsert_summary(liker_account, "sent_likes")

        logging.warning(f"{liker_account} liked {liked_account}'s post")

    def add_follow_request(self, requester_account, requested_account):
        self.c.execute(f"INSERT INTO follow_requests (requester_account, requested_account, accepted, declined, client_id) VALUES ('{requester_account}', '{requested_account}', 0, 0, '{self.client_id}');")
        self.conn.commit()

        self.upsert_summary(requester_account, "sent_requests")

        logging.warning(f"{requester_account} send follow request to {requested_account}")

    def add_dm(self, sender_account, sent_account, message):
        self. c.execute(f"INSERT INTO dm (sender_account, sent_account, message, client_id) VALUES ('{sender_account}', '{sent_account}', '{message}', '{self.client_id}');")
        self.conn.commit()

        self.upsert_summary(sender_account, "sent_dm")

        logging.warning(f"{sender_account} send dm to {sent_account}")

    def find_follow_requests(self, requester_account, days):
        usernames = []

        self.c.execute(f"SELECT requested_account FROM follow_requests WHERE client_id='{self.client_id}' AND requester_account='{requester_account}' AND request_date < to_timestamp('now', '-{days} days');")
        rows = self.c.fetchall()

        for row in rows:
            usernames.append(row[0])

        return usernames

    def delete_follow_request(self, requester_account, requested_account):
        self.c.execute(f"DELETE FROM follow_requests WHERE client_id='{self.client_id}' AND requester_account='{requester_account}' AND requested_account='{requested_account}';")
        self.conn.commit()

    def add_blacklist(self, account):
        self.c.execute(f"INSERT INTO blacklist (account, request_declined, client_id) VALUES ('{account}', 0, '{self.client_id}');")
        self.conn.commit()

        logging.warning(f"{account} has been added to blacklist")

    def in_blacklist(self, account):
        self.c.execute(f"SELECT * FROM blacklist WHERE client_id='{self.client_id}' AND account='{account}';")
        if self.c.fetchone():
            logging.warning(f"{account} is in blacklist, so skipping\n")
            return True

        return False

    def add_user(self, user):
        try:
            self.c.execute(f"INSERT INTO users (account, client_id) VALUES ('{user}', '{self.client_id}');")
            self.conn.commit()

            logging.warning(f"{user} has been added to users")
        except:
            pass

    def get_dm_profile(self, profile_name):
        self.c.execute(f"SELECT * FROM dm_profiles WHERE client_id='{self.client_id}' AND profile_name='{profile_name}';")
        rows = self.c.fetchall()

        messages = []
        for row in rows:
            messages.append(row[1])

        return messages

    def upsert_summary(self, account, column_name):
        sent_likes = 1 if column_name == "sent_likes" else 0
        sent_requests = 1 if column_name == "sent_requests" else 0
        sent_dm = 1 if column_name == "sent_dm" else 0

        self.c.execute(
            f"INSERT INTO summary(summary_id, account, sent_likes, sent_requests, sent_dm, client_id) VALUES('{self.UUID}', '{account}', {sent_likes}, {sent_requests}, {sent_dm}, '{self.client_id}') ON CONFLICT (summary_id) DO UPDATE SET {column_name} = summary.{column_name} + 1;")
        self.conn.commit()

    def close_conn(self):
        self.c.close()
        self.conn.close()
