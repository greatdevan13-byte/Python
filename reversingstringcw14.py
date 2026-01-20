import random
import math
names=["Ramesh","Suresh","Satish","Arathy","Satish","Ramesh","Rajesh","Padmaraj","Susheela","Anjali","Maneesh"]
newlist_names=list(set(names))

random_name=random.choice(newlist_names)
reversed_name = "".join(reversed(random_name))
print("The randomly chosen reversed name :",reversed_name)

count=0
for x in newlist_names:
    count+=1

print("Count of unique names :",count) 

rounded_count=math.sqrt(math.floor(count))
print("Square root of the count :",rounded_count)
