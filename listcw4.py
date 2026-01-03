fruits=["Apple","Orange","Kiwi"]
veg=["Tomato","Carrot","Beetroot"]
beverages=["Tea","Coffee","Cold coffee"]
fruits.append("Avacado")
veg.insert(1,"Cucumber")
beverages.pop()

inventory=fruits+veg+beverages

print("New Fruit list :",fruits)
print("New veg list :",veg)
print("New beverages list :",beverages)
print("Combined list :",inventory)


print(fruits[:1])
 
print(fruits[-1])

print("water" in beverages)

first_items = (fruits[0], veg[0], beverages[0])
print("First items :",first_items)

