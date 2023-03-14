from random import randint
from user import User

class Organization :
    def __init__(self, organization_name : str, organization_logo : str = "default_logo_image.png") :
        self.__organization_id = randint(10000000, 100000000);
        self.__organization_name = organization_name
        self.__organization_logo = organization_logo
        self.__organization_member = []
        self.__notifications = []
        self.__projects = []
        self.__activity_thread = []

    def show_projects(self) :
        if self.__projects is not None:
            for p in self.__projects :
                print(p)