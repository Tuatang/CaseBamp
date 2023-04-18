from fastapi import FastAPI
from datetime import datetime
from typing import List

app = FastAPI()

class User:
    def __init__(self, username):
        self.username = username
        self.notifications = []

    def add_notification(self, notification):
        self.notifications.append(notification)

class Notification:
    numeric_id = 0
    def __init__(self, title: str, details: str, timestamp: datetime, sender: User, receivers: List[User]):
        self.title = title
        self.id = "8" + "{:07d}".format(Notification.numeric_id)
        self.details = details
        self.timestamp = timestamp
        self.sender = sender
        self.receivers = receivers
        Notification.numeric_id += 1

    def send_notification(self):
        for receiver in self.receivers:
            receiver.add_notification(self)

class Activity:
    def __init__(self, title: str, detail: str, timestamp: datetime, users: List[User]):
        self.title = title
        self.detail = detail
        self.timestamp = timestamp
        self.accomplished_by = users

    def __str__(self):
        return f'Activity: {self.title}, Description: {self.detail}, Timestamp: {self.timestamp}, Accomplished by: {self.accomplished_by}'

users = [User('Jack'), User('Mam'), User('King')]

@app.post('/notification')
async def create_notification(title: str, details: str, sender: str, receivers: List[str]):
    sender_obj = next((user for user in users if user.username == sender), None)
    receiver_objs = [user for user in users if user.username in receivers]
    notification = Notification(title=title, details=details, timestamp=datetime.now(), sender=sender_obj, receivers=receiver_objs)
    notification.send_notification()
    return {'message': 'Notification sent successfully'}

@app.post('/activity')
async def create_activity(title: str, detail: str, users: List[str]):
    user_objs = [user for user in users if user.username in users]
    activity = Activity(title=title, detail=detail, timestamp=datetime.now(), users=user_objs)
    return {'message': 'Activity created successfully', 'activity': str(activity)}
