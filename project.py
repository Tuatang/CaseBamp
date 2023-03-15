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
        #self.__schedule = schedule
        #self.__message_board = message_board

    def __str__(self) :
        return ("Name :" + self.__project_name + " Description :" + self.__project_description 
    + " Interval :" + self.__start_date + "," + self.__end_date)