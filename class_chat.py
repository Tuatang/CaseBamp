class Chat:
    def __init__(self, message_title, message_id, content, timestamp, added_by, notify_users, received_users):
        self.message_title = message_title
        self.message_id = message_id
        self.content = content
        self.timestamp = timestamp
        self.added_by = added_by
        self.notify_users = notify_users
        self.received_users = received_users

    def delete_chat(self):
       
        pass

    def create_chat(self, message_title, content, added_by, notify_users, received_users):
      
        pass

    def edit_chat(self, message_title=None, content=None, added_by=None, notify_users=None, received_users=None):
      
        pass
