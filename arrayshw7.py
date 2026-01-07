inventory=[]

def add_items(item):
    inventory.append(item)


def count_items(items):
    if not items:
        return 0
    return 1+count_items(items[1:])  

def main():
    add_items("Dog food")  
    add_items("Cat toy")  
    add_items("Bird cage")  
    add_items("Fish tank")  
main()    


show_item=lambda item:print("Item in stock :",item)

for item in inventory:
    show_item(item)

total_items=count_items(inventory)
print("Total number of items in stock :",total_items)    

