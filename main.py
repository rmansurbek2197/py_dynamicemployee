class EmployeeSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, *skills, **info):
        employee = {
            "skills": skills,
            "info": info,
            "salary": info.get("salary", 0)
        }
        self.employees.append(employee)
        return employee

    def give_bonus(self, name, bonus):
        for emp in self.employees:
            if emp["info"].get("name") == name:
                emp["salary"] += bonus
                return emp

    def filter_by_skill(self, skill):
        return [e for e in self.employees if skill in e["skills"]]


system = EmployeeSystem()

system.add_employee("Python", "SQL", name="Ali", salary=1000)
system.add_employee("Java", "Spring", name="John", salary=1200)

system.give_bonus("Ali", 300)

print(system.filter_by_skill("Python"))
