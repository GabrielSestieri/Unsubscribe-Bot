from simplegmail import Gmail
from simplegmail.query import construct_query


def retrieve_senders():
    gmail = Gmail()
    query_params = {
        "newer_than": (5, "day"),
        "older_than": (1, "day"),
    }
    messages = gmail.get_messages(query=construct_query(query_params))
    senders = []
    for message in messages:
        loc1 = str(message.sender).find("<")
        loc2 = str(message.sender).find(">")
        sender_email = message.sender[loc1+1:loc2]
        senders.append(sender_email)
    cleaned_senders = set(senders)
    with open("senders.txt", "a") as f:
        for sender in cleaned_senders:
            f.write(sender + "\n")










 
