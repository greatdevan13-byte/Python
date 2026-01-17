import re

try:
    title = input("Enter book title: ")

 
    if not re.fullmatch("[a-zA-Z ]+", title):
        raise ValueError("Invalid title")

    year = input("Enter publication year: ")

  
    if not re.fullmatch("(19|20)[0-9]{2}", year):
        raise ValueError("Invalid publication year")

    print("\nBook details accepted")
    print("Title:", title)
    print("Year:", year)

except:
    print("\nError: Invalid input")

finally:
    print("\nProgram ended")
