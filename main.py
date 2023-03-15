from event import Event
from datetime import datetime

def main():
    # Create an event
    event_1 = Event(datetime(2015, 11, 5, 10, 0), datetime(2015, 11, 5, 11, 0), "Python Class", "Learn Python")
    print(event_1)
    
if __name__ == "__main__":
    main()