class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return "Name: {}, Age: {}".format(self.name, self.age)

class Employee:
    def __init__(self, employee_id, job_title):
        self.employee_id = employee_id
        self.job_title = job_title

    def display_employee_info(self):
        return "Employee ID: {}, Job Title: {}".format(self.employee_id, self.job_title)

class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        return "Student ID: {}, Major: {}".format(self.student_id, self.major)

class PersonInfo(Employee, Student, Person):
    def __init__(self, name, age, employee_id, job_title, student_id, major):
        # Call the constructors of both parent classes
        Employee.__init__(self, employee_id, job_title)
        Student.__init__(self, student_id, major)
        Person.__init__(self, name, age)

    def display_person_info(self):
        person_info = self.display_info()
        employee_info = self.display_employee_info()
        student_info = self.display_student_info()
        return "{}\n{}\n{}".format(person_info, employee_info, student_info)

person_info = PersonInfo(name="Ankita", age=20, employee_id="E", job_title="Developer", student_id="S456", major="Computer Science")

print("Person Information:")
print(person_info.display_person_info())