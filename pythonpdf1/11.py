class Vehicle:
    def drive(self):
        return "Generic vehicle is being driven."

class Car(Vehicle):
    def drive(self):
        return "Car is on the road. Vroom, vroom!"

class Bicycle(Vehicle):
    def drive(self):
        return "Bicycle is pedaling along. Ding, ding!"

generic_vehicle = Vehicle()
car = Car()
bicycle = Bicycle()

print("Generic Vehicle:", generic_vehicle.drive())  
print("Car:", car.drive())                          
print("Bicycle:", bicycle.drive())                  