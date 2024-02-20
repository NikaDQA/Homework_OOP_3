class Employee:

    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def work(self):
        return "I come to the office."

    def __str__(self):
        return f"Employee: {self.name}"

    def __lt__(self, other):
        return self.daily_salary < other.daily_salary

    def __gt__(self, other):
        return self.daily_salary > other.daily_salary

    def __eq__(self, other):
        return self.daily_salary == other.daily_salary

    def check_salary(self, days):
        return self.daily_salary * days


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return f"Recruiter: {self.name}"


class Developer(Employee):

    def __init__(self, name, daily_salary, tech_stack):
        super().__init__(name, daily_salary)
        self.tech_stack = tech_stack

    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        return f"Developer: {self.name}, Tech Stack: {self.tech_stack}"

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __add__(self, other):
        name = self.name + ' ' + other.name
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        daily_salary = max(self.daily_salary, other.daily_salary)
        return Developer(name, daily_salary, tech_stack)


developer1 = Developer("Dima", 400, ["Python", "Java"])
developer2 = Developer("Anton", 350, ["C++"])

print(developer1)
print(developer2)

print(developer1 == developer2)
print(developer1 < developer2)
print(developer1 > developer2)

print("Salary for 10 days:", developer1.check_salary(10))
print("Salary for 10 days:", developer2.check_salary(10))
print("Max daily salary:", max(developer1.daily_salary, developer2.daily_salary))

new_developer = developer1 + developer2
print(new_developer, max(developer1.daily_salary, developer2.daily_salary))
