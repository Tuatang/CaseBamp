from datetime import datetime
class Event:
    def __init__(self, starts, ends, title, content):
        self.__starts = starts
        self.__ends = ends
        self.__title = title
        self.__content = content
        assigned_to = [] # list of users
        notify_to = [] # list of users
    
    def __str__ (self):
        return "Event: " + self.__title + " starts at " + str(self.__starts) + " and ends at " + str(self.__ends)