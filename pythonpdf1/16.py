import datetime

class Room:
    def __init__(self, room_number, capacity, rate_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.rate_per_night = rate_per_night
        self.is_booked = False

class Guest:
    def __init__(self, guest_name, contact_number):
        self.guest_name = guest_name
        self.contact_number = contact_number

class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def generate_invoice(self):
        total_nights = (self.check_out_date - self.check_in_date).days
        total_cost = total_nights * self.room.rate_per_night
        return f"Invoice for {self.guest.guest_name}:\nRoom: {self.room.room_number}\nTotal Nights: {total_nights}\nTotal Cost: ${total_cost}"

class HotelReservationSystem:
    def __init__(self):
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_room_availability(self, room_number, check_in_date, check_out_date):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_booked:
                return True
        return False

    def book_room(self, guest, room_number, check_in_date, check_out_date):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_booked:
                room.is_booked = True
                reservation = Reservation(guest, room, check_in_date, check_out_date)
                self.reservations.append(reservation)
                return reservation
        return None


hotel = HotelReservationSystem()

room1 = Room(room_number=101, capacity=2, rate_per_night=100)
room2 = Room(room_number=102, capacity=3, rate_per_night=120)

hotel.add_room(room1)
hotel.add_room(room2)

guest1 = Guest(guest_name="Ankita", contact_number="123-456-7890")

check_in_date = datetime.date(2023, 1, 15)
check_out_date = datetime.date(2023, 1, 20)

if hotel.check_room_availability(room_number=101, check_in_date=check_in_date, check_out_date=check_out_date):
    reservation = hotel.book_room(guest1, room_number=101, check_in_date=check_in_date, check_out_date=check_out_date)
    if reservation:
        print("Room booked successfully!")
        print(reservation.generate_invoice())
    else:
        print("Room booking failed. Room may already be booked.")
else:
    print("Room not available for the selected dates.")