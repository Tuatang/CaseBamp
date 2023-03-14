class User :
    def __init__(self, email : str, name : str, phone : str) :
        self.__email = email
        self.__name = name
        self.__phone = phone
        self.__organization = []
        self.__user_assignment = []
        self.__user_draft = []
        self.__user_schedule = []
        self.__is_out_of_office = False

        self.__admin = False
        self.__owner = False
    
    def out_of_office(self) :
        pass

    def create_project(self, name, description, start_date, end_date) :
        pass