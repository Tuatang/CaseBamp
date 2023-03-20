from datetime import datetime
from random import randint

class Element:
    def __init__(self, title, id):
        self.__title = title
        self.__id = id
        self.__in_trash = False

class Content:
    def __init__(self, details):
        self.__details = details

class Message(Element):
    numberic_id = 0
    id = "500" + str(numberic_id)
    def __init__(self, title, content:Content, timestamp:datetime):
        super.__init__(self, title, id)
        self.__content = content
        self.__timestamp = timestamp
        self.__in_trash = False

        numberic_id += 1
        id += str(numberic_id)

    def __str__ (self):
        return "Message: " + self.__title + " at " + str(self.__timestamp)
    def set_attribute(self, attribute, value):
        pass

class MessageBoard:
    def __init__(self, title = "Message Board"):
        self.__title = title
        self.__messages = [] # list of messages

    def get_message(self):
        pass
    def save_message(self):
        pass
    def edit_message(self):
        pass

class Chat:
    def __init__(self, content:Content, timestamp:datetime, added_by):
        self.__content = content
        self.__timestamp = timestamp
        self.__added_by = added_by

class ChatHistory:
    thread_id = randint(100000, 1000000)
    def __init__(self, thread:list, received_users:list):
        self.__thread = thread
        self.__received_users = received_users
    def update_chat_history(self):
        pass
    def get_chat(self):
        pass
    def edit_chat(self, chat: Chat, attribute, value):
        pass

class Event(Element):
    numberic_id = randint(0, 100);
    id = "600" + str(numberic_id)
    def __init__(self, title, note:Content, starts_at:datetime, ends_at:datetime,all_day:bool, paticipants:list):
        super.__init__(self, title)
        self.__note = note
        self.__starts_at = starts_at
        self.__ends_at = ends_at
        self.__all_day = all_day
        self.__paticipants = paticipants

        numberic_id += 1
        id += str(numberic_id)
        

    def set_attribute(self, attribute, value):
        pass