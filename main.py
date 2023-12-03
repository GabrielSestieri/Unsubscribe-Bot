from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

query_params = {
    "newer_than": (30, "day"),
    "older_than": (1, "day"),
}

messages = gmail.get_messages(query=construct_query(query_params))

for message in messages:
    print(message)