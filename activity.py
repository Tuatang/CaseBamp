class ActivityLog :
    def __init__(self) :
        self.__activity_list = []

    def generate_activity(self, detail, timestamp, users) :
        pass

    def save_activity(self, activity) :
        self.__activity_list.append(activity)

    def get_activity(self) :
        if self.__activity_list != None:
            return self.__activity_list
        
class Activity :
    def __init__(self, detail, timestamp, users) :
        self.__detail = detail
        self.__timestamp = timestamp
        self.__accomplished_by = users