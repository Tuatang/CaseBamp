from messageandchat import *
from datetime import datetime
from useraccount import *

def main():
    account = Account("pond", "pond1234")
    user1 = User("65010539@kmitl.ac.th", "Pond", "0812345678", "KMITL", False, False)
    user1.edit_profile("Pond", "0812345678")
    noti1 = Notification("Notification 1", Content("Details"), datetime.now(), "User 1", ["User 1", "User 2"])
    noti2 = Notification("Notification 2", Content("Details"), datetime.now(), "User 2", ["User 1", "User 2"])
    noti1.send_notification(user1)
    noti2.send_notification(user1)

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
from organization import Organization

def main() :
    organization_1 = Organization("KMITL")
    organization_1.create_project("Sleep", "Relax", "15-03-2023", "20-03-2023")
    organization_1.show_projects()

#edit
if __name__ == "__main__" :
    main()