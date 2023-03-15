from random import randint
from project import Project

class Organization :
    def __init__(self, organization_name) :
        self.__organization_id = randint(10000000, 100000000);
        self.__organization_name = organization_name
        # self.__organization_logo = organization_logo
        self.__organization_member = []
        self.__notifications = []
        self.__projects = []
        self.__activity_thread = []

    def create_project(self, name, description, start_date, end_date) :
        name = Project(name, description, start_date, end_date)
        self.__projects.append(name)

    def show_projects(self) :
        if self.__projects is not None:
            for p in self.__projects :
                print(p)