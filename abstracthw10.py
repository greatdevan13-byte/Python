from abc import ABC , abstractmethod

class user(ABC):
    def __init__(self,name,account_year):
        self.name=name
        self.year=account_year

    def account_age(self):
        current_year=2025   
        return current_year-self.year

    @abstractmethod
    def get_role(self):
     pass

class admin(user):
    def get_role(self):
     return "Admin"


    def __str__(self):
       return f"{self.name} is an admin user"

class guest(user):
   def get_role(self):
      return "Guest"

   def __str__(self):
      return f"{self.name} is an guest user"
   
admin_user=admin("Ramu",2018)
guest_user=guest("Sumesh",2021)   

print("Role :",admin_user.get_role())
print("Account age :",admin_user.account_age())
print(admin_user)

print("Role :",guest_user.get_role())
print("Account age :",guest_user.account_age())
print(guest_user)
          
          
