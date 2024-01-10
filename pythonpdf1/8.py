class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Create an object of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022)

print("Car Details:")
print("Make:", my_car.make)
print("Model:", my_car.model)
print("Year:", my_car.year)