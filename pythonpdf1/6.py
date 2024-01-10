class Vehicle:
    color = "Red"  
    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = 0.1 * base_fare  # 10% maintenance charge for buses
        total_fare = base_fare + maintenance_charge
        return total_fare


vehicle1 = Vehicle(50)
bus1 = Bus(40)

print("Color of Vehicle 1:", vehicle1.color)  
print("Color of Bus 1:", bus1.color)          