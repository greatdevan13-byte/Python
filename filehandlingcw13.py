
item = input("Enter a new stationery item: ")


file = open("items.txt", "a+")

file.write(item + "\n")

file.seek(0)

items_list = file.read()


file.close()


print("\n📋 List of Stationery Items:")
print(items_list)
