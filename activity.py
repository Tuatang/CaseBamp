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
        
    def show_activity(self) :
        if self.__activity_list is not None:
            for a in self.__activity_list :
                print(a)
        
class Activity :
    def __init__(self, detail, timestamp, users) :
        self.__detail = detail
        self.__timestamp = timestamp
        self.__accomplished_by = users

    def __str__(self) :
        return 'Activity: ' + str(self.__detail) + ' Timestamp: ' + str(self.__timestamp) + ' Accomplished by: ' + str(self.__accomplished_by)