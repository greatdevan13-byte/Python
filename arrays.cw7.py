my_list= ["milk", "bread", "eggs"]

def add_item(item): 
 my_list.append(item)

def remove_last_item():
 my_list.pop() 

display_item= lambda item:print("Item :",item)

def count_characters(items):
    if len(items) == 0:     
        return 0
    return len(items[0]) + count_characters(items[1:])

add_item("Soda")
remove_last_item()
for item in my_list:
  display_item(item)

total_chars=count_characters(my_list)
print("Totsl characters :",total_chars)  






