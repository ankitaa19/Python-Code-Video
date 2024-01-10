import datetime

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.projects = []

    def log_hours(self, project, hours, date):
        time_entry = TimeEntry(project, hours, date)
        self.projects.append(time_entry)

    def generate_timesheet(self, start_date, end_date):
        timesheet = {}
        for entry in self.projects:
            if start_date <= entry.date <= end_date:
                if entry.project.name not in timesheet:
                    timesheet[entry.project.name] = 0
                timesheet[entry.project.name] += entry.hours
        return timesheet

    def calculate_overtime(self, start_date, end_date, standard_hours_per_week):
        total_hours = sum(self.generate_timesheet(start_date, end_date).values())
        overtime_hours = max(0, total_hours - standard_hours_per_week)
        return overtime_hours

class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name

class TimeEntry:
    def __init__(self, project, hours, date):
        self.project = project
        self.hours = hours
        self.date = date

employee1 = Employee(employee_id=1, name="Ankita")
project1 = Project(project_id=101, name="Project A")

# Hours for employee1 on project1
employee1.log_hours(project1, hours=8, date=datetime.date(2023, 1, 15))
employee1.log_hours(project1, hours=6, date=datetime.date(2023, 1, 16))

# Timesheet for employee1 for a specific date range
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 1, 31)
timesheet = employee1.generate_timesheet(start_date, end_date)
print("Timesheet for {} from {} to {}:".format(employee1.name, start_date, end_date))
for project, hours in timesheet.items():
    print("{}: {} hours".format(project, hours))

# Calculate overtime
standard_hours_per_week = 40
overtime_hours = employee1.calculate_overtime(start_date, end_date, standard_hours_per_week)
print("Overtime for {} from {} to {}: {} hours".format(employee1.name, start_date, end_date, overtime_hours))