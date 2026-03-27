import datetime
from typing import List

class Person:
    def __init__(self, name, age, email, phone):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__phone = phone
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @property
    def email(self):
        return self.__email
    @property
    def phone(self):
        return self.__phone
    def display_info(self):
        print(self)

class Employee(Person):
    def __init__(self, name, age, email, phone, employee_id, department, salary, join_date):
        super().__init__(name, age, email, phone)
        self.__employee_id = employee_id
        self.__department = department
        self.__salary = salary
        self.__join_date = join_date
    @property
    def employee_id(self):
        return self.__employee_id
    @property
    def department(self):
        return self.__department
    @property
    def salary(self):
        return self.__salary
    @property
    def join_date(self):
        return self.__join_date
    def calculate_salary(self):
        return self.__salary
    def get_experience(self):
        today = datetime.date.today()
        delta = today - self.__join_date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        return f"{years} year(s) {months} month(s)"
    def __str__(self):
        return (f"{self.name} | ID: {self.employee_id} | "
                f" Dept: {self.department} | "
                f"Salary: {self.calculate_salary()} | "
                f"Experience: {self.get_experience()}")

class Manager(Employee):
    def __init__(self, name, age, email, phone, employee_id, department, salary, join_date, bonus):
        super().__init__(name, age, email, phone, employee_id, department, salary, join_date)
        self.__bonus = bonus
        self.__team_members: List[Employee] = []
    @property
    def bonus(self):
        return self.__bonus
    def add_team_member(self, employee: Employee):
        if not isinstance(employee, Employee):
            return "Only Employee instances can be added"
        flag = 0
        for emp in self.__team_members:
            if emp.employee_id == employee.employee_id:
                flag = 1
                break
        if flag == 0:
            self.__team_members.append(employee)
            return "Employee added successfully"
        else:
            return "Employee already exists"
    def calculate_salary(self):
        return self.salary + self.__bonus
    def __str__(self):
        return (f"{self.name} | ID: {self.employee_id} | "
                f" Dept: {self.department} | "
                f"Salary: {self.calculate_salary()} | "
                f"Experience: {self.get_experience()} | "
                f"Team members: {[team_member for team_member in self.__team_members]}")

class Developer(Employee):
    def __init__(self, name, age, email, phone, employee_id, department, salary, join_date, programming_languages= None, projects = None):
        super().__init__(name, age, email, phone, employee_id, department, salary, join_date)
        self.__programming_languages = list(programming_languages) if programming_languages else []
        self.__projects = list(projects) if projects else []
    @property
    def programming_languages(self):
        return self.__programming_languages
    @property
    def projects(self):
        return self.__projects
    def add_skill(self, skill):
        flag = 0
        for lang in self.__programming_languages:
            if lang.lower() == skill.lower():
                flag = 1
                break
        if flag == 0:
            self.__programming_languages.append(skill)
            return f"{skill} added successfully"
        else:
            return f"This developer already has {skill}"
    def assign_project(self, project):
        flag = 0
        for proj in self.__projects:
            if proj.lower() == project.lower():
                flag = 1
                break
        if flag == 0:
            self.__projects.append(project)
            return f"{project} added successfully"
        else:
            return f"This developer already has {project}"
    def __str__(self):
        return (f"{self.name} | ID: {self.employee_id} | "
                f" Dept: {self.department} | "
                f"Salary: {self.calculate_salary()} | "
                f"Experience: {self.get_experience()} | "
                f"Skills: {self.__programming_languages} | "
                f"Projects: {self.__projects}")

class Intern(Employee):
    def __init__(self, name, age, email, phone, employee_id, department, join_date, mentor, duration, stipend):
        super().__init__(name, age, email, phone, employee_id, department, salary = 0, join_date = join_date)
        self.__mentor = mentor
        self.__duration = duration
        self.__stipend = stipend
    @property
    def mentor(self):
        return self.__mentor
    @property
    def duration(self):
        return self.__duration
    @property
    def stipend(self):
        return self.__stipend
    def calculate_salary(self):
        return self.__stipend
    def __str__(self):
        return (f"{self.name} | ID: {self.employee_id} | "
                f" Dept: {self.department} | "
                f"Stipend: {self.calculate_salary()} | "
                f"Duration: {self.__duration}")

class Company:
    def __init__(self):
        self.__employees = []
    @property
    def employees(self):
        return self.__employees
    def hire_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            return "Only Employee instances can be added"
        flag = 0
        for emp in self.__employees:
            if emp.employee_id == employee.employee_id:
                flag = 1
                break
        if flag == 0:
            self.__employees.append(employee)
            return "Employee hired successfully"
        else:
            return "Employee already exists"
    def fire_employee(self, employee_id):
        for index, emp in enumerate(self.__employees):
            if emp.employee_id == employee_id:
                self.__employees.pop(index)
                return "Employee fired successfully"
        return "Employee not found"
    def promote_employee(self, employee_id, new_role):
        for index, employee in enumerate(self.__employees):
            if employee.employee_id == employee_id:
                if new_role.lower() == "developer":
                    promoted = Developer(employee.name, employee.age, employee.email, employee.phone, employee.employee_id, employee.department, employee.salary, employee.join_date)
                elif new_role.lower() == "manager":
                    promoted = Manager(employee.name, employee.age, employee.email, employee.phone, employee.employee_id, employee.department, employee.salary, employee.join_date, bonus=20000)
                else:
                    return "Invalid Role"
                self.__employees[index] = promoted
                return f"Employee promoted to {new_role}"
        return "Employee not found"
    def get_department_employees(self, department):
        return [employee for employee in self.__employees if employee.department.lower() == department.lower()]
    def calculate_total_payroll(self):
        return sum(employee.calculate_salary() for employee in self.__employees)
    def display_all_employees(self):
        for e in self.__employees:
            print(e)

def main():
    company = Company()
    emp1 = Employee("Alice", 30, "alice@mail.com", "99999", 101, "IT", 60000, datetime.date(2019, 6, 10))
    dev1 = Developer("Bob", 27, "bob@mail.com", "88888", 102, "IT", 50000, datetime.date(2021, 1, 15), ["Python"],
                     ["HR System"])
    intern1 = Intern("Charlie", 22, "charlie@mail.com", "77777", 103, "IT", datetime.date(2024, 1, 1), mentor="Alice",
                     duration=6, stipend=15000)

    company.hire_employee(emp1)
    company.hire_employee(dev1)
    company.hire_employee(intern1)

    company.display_all_employees()

    print(company.calculate_total_payroll())

    print(company.promote_employee(102, "Manager"))

    company.display_all_employees()

if __name__ == "__main__":
    main()
