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
        self.__activity_log = []

    def add_project(self, project) :
        self.__projects.append(project)

    def create_project(self, name, description, start_date, end_date) :
        name = Project(name, description, start_date, end_date)
        self.add_project(name)
        
    def add_owner(self, user) :
        pass

    def add_member(self, user) :
        self.__organization_member.append(user)

    def get_activity_log(self) :
        return self.__activity_log
    
    def get_project(self) :
        return self.__projects

    def generate_activity(self) :
        pass

    def generate_notification(self) :
        pass

    def check_project_for_access(self, user, project) :
        pass

    def cancel_an_organization(self) :
        pass

    def set_organization_name(self, newname) :
        pass

    def create_message_board(self, title) :
        pass

    def create_chat_history(self, receivers) :
        pass

    def search_user(self, username) :
        pass

    def create_content(self, detail) :
        pass

    def invite_user(self, name, email, phone, job_title) :
        pass

    def send_invite_request(self) :
        pass

    def check_user_for_admin_role(self, user) :
        pass

    def set_admin(user) :
        pass