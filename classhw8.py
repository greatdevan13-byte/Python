class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name :", self.name)
        print("Role :", self.role)


class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        Employee.display(self)
        print("Specialization :", self.specialization)


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        Employee.display(self)
        print("Yoga Style :", self.yoga_style)


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        Employee.display(self)
        print("Specialization :", self.specialization)
        print("Yoga Style :", self.yoga_style)



employee1 = Employee("Ramu", "Cleaner")
trainer1 = Trainer("Raj", "Trainer", "Cardio")
yoga1 = YogaInstructor("Anita", "Instructor", "Shavasanam")
multi1 = MultiTrainer("Ramesh", "Multi Trainer", "Strength Training", "Kukudasanam")

print("Employee details:")
employee1.display()

print("\nTrainer details:")
trainer1.display()

print("\nYoga instructor details:")
yoga1.display()

print("\nMulti trainer details:")
multi1.display()
