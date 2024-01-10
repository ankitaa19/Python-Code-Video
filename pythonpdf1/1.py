from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, '%Y-%m-%d')  

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

person1 = Person("Ankita Lokhande", "India", "2003-04-19")
age = person1.calculate_age()

print(f"{person1.name} from {person1.country} is {age} years old.")