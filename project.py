from random import randint
from datetime import datetime

class Project :
    def __init__(self, project_name : str, project_description : str, start_date : datetime, end_date : datetime) :
        self.__project_id = randint(10000000, 100000000);
        self.__project_name = project_name
        self.__project_description = project_description
        self.__start_date = start_date
        self.__end_date = end_date
        self.__accessable_users = []
        self.__todo_topics = []
        self.__events = []
        # self.__documents_and_files = documents_and_file_folder
        # self.__campfire_chat = chat_history
        # self.__message_board = message_board
        self.__in_trash = False

    def __str__ (self):
        return 'Project: ' + str(self.__project_name) + ' Description: ' + str(self.__project_description) + ' Interval: ' + str(self.__start_date) + ' :: ' + str(self.__end_date)

    def get_todo_topics(self) :
        if self.__todo_topics != None:
            return self.__todo_topics
    
    def get_events(self) :
        if self.__events != None:
            return self.__events
        
    def create_documents_and_files_folder(self, title) :
        pass

    def get_documents_and_files(self) :
        pass

    def get_message_board(self) :
        pass

    def get_campfire_chat(self) :
        pass

    def create_todo_topic(self, title, description) :
        pass

    def save_todo_topic(self, todo_topic) :
        pass

    def edit_todo_topic(self, todo_topic, title, description) :
        pass

    def check_event_for_assigned(self, event, user) :
        pass

    def check_project_for_todo(self, to_do, user) :
        pass

    def create_event(self, title, note, start_date, end_date) :
        pass

    def save_event(self, event) :
        self.__events.append(event)

    def edit_event(self, event, title, note, start_date, end_date) :
        pass

    def add_member(self, user) :
        self.__accessable_users.append(user)

    def remove_member(self, user) :
        pass