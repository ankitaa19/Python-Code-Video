import datetime

class Room:
    def __init__(self, room_id, room_name, capacity):
        self.room_id = room_id
        self.room_name = room_name
        self.capacity = capacity
        self.reservations = []

    def check_availability(self, start_time, end_time):
        for reservation in self.reservations:
            if not (end_time <= reservation.start_time or start_time >= reservation.end_time):
                return False  # Room is not available
        return True

    def book_room(self, user, start_time, end_time):
        if self.check_availability(start_time, end_time):
            reservation = Reservation(user, self, start_time, end_time)
            self.reservations.append(reservation)
            return reservation
        else:
            return None  # Room is already booked 

class User:
    def __init__(self, user_id, user_name, email):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email

class Reservation:
    def __init__(self, user, room, start_time, end_time):
        self.user = user
        self.room = room
        self.start_time = start_time
        self.end_time = end_time

    def send_notification(self):
        print("Notification sent to {}: Your reservation for {} on {} to {} is confirmed.".format(
            self.user.user_name, self.room.room_name, self.start_time, self.end_time))

# User input for reservation details
user_name = input("Enter your name: ")
email = input("Enter your email: ")
user_id = int(input("Enter your user ID: "))
start_time_str = input("Enter reservation start time (YYYY-MM-DD HH:MM): ")
end_time_str = input("Enter reservation end time (YYYY-MM-DD HH:MM): ")

# Creating User and Reservation objects
user1 = User(user_id, user_name, email)
start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')
end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')

room1 = Room(room_id=1, room_name="Conference Room 1", capacity=10)

# Book room for user1 with user input
reservation = room1.book_room(user1, start_time, end_time)

if reservation:
    print("Room booked successfully by {}!".format(user1.user_name))
    reservation.send_notification()
else:
    print("Room not available for the requested time slot.")