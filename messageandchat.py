from datetime import datetime
from random import randint
class User:
    def __init__(self, email, name, phone, organization, is_admin = False, is_owner = False):
        self.__email = email
        self.__name = name
        self.__phone = phone
        self.__organization = organization
        self.__is_admin = is_admin
        self.__is_owner = is_owner
        self.__list_of_private_chat = []
        self.__list_of_notification = []

    def set_owner_role(self, is_owner):
        self.__is_owner = is_owner
    def set_admin_role(self, is_admin):
        self.__is_admin = is_admin
    def  check_user_for_chat_history(self, user, chat_history):
        pass
    def search_chat_history(self, sender, receiver):
        pass
    def get_chat_history(self):
        pass
    def get_notification(self):
        pass
    def edit_profile(self, name, phone):
        pass
    def request_chat(self, chat_type: str):
        pass
    def get_private_chat(self):
        pass

class Account:
    def __init__(self, account_email, account_password):
        self.__account_email = account_email
        self.__account_password = account_password
        self.__account_users = []
    
    def log_out(self):
        pass

class Notification:
    def __init__(self, title, details, timestamp:datetime, sender, receivers:list):
        self.__title = title
        self.__id = randint(100000, 1000000)
        self.__details = details
        self.__timestamp = timestamp
        self.__sender = sender
        self.__receivers = receivers

    def send_notification(self, user:User):
        pass