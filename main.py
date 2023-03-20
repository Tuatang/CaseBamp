from messageandchat import *
from datetime import datetime

def main():
    message1 = Message("Message 1", Content("Details"), datetime.now())
    message2 = Message("Message 2", Content("Details"), datetime.now())

    message_boad = MessageBoard()
    message_boad.save_message(message1)
    message_boad.save_message(message2)

    chat1 = Chat(Content("Details"), datetime.now(), "User 1")
    chat2 = Chat(Content("Details"), datetime.now(), "User 2")

    chat_history = ChatHistory([chat1, chat2], ["User 1", "User 2"])

    event1 = Event("Event 1", Content("Details"), datetime.now(), datetime.now(), True, ["User 1", "User 2"])
    event2 = Event("Event 2", Content("Details"), datetime.now(), datetime.now(), True, ["User 1", "User 2"])


    
if __name__ == "__main__":
    main()

#edit