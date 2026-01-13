from abc import ABC, abstractmethod   # used to make abstract class

# Step 1: Create an abstract User class
class User(ABC):

    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    # Step 2: method to calculate years on platform
    def years_on_platform(self):
        current_year = 2025
        return current_year - self.joining_year

    # abstract method (must be implemented by child classes)
    @abstractmethod
    def show_details(self):
        pass

class Customer(User):

    def show_details(self):
        print("Name :", self.name)
        print("Role : Customer")
        print("Years on platform :", self.years_on_platform())

class Vendor(User):

    def show_details(self):
        print("Name :", self.name)
        print("Role : Vendor")
        print("Years on platform :", self.years_on_platform())

c1 = Customer("Deva", 2021)
v1 = Vendor("Ramesh", 2018)

c1.show_details()
v1.show_details()




       