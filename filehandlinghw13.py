
filename = "students.txt"


print("Existing student names:")

try:
    file = open(filename, "r")
    print(file.read())
    file.close()
except:
    print("No student names found.")

n = int(input("\nHow many student names do you want to add? "))


file = open(filename, "a")

for i in range(n):
    name = input("Enter student name: ")
    file.write(name + "\n")

file.close()
print("\nNames saved successfully!")


print("\nAll student names:")

file = open(filename, "r")
print(file.read())
file.close()
