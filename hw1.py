rice,sugar,oil=45,40,130
rice_qty,sugar_qty,oil_qty=3,2.5,1.8
total_cost=(rice*rice_qty)+(sugar*sugar_qty)+(oil*oil_qty)
print(total_cost)
total_int=int(total_cost)
print(total_int)
total_str=str(total_int)
print(total_str)
import random
rand_num=random.randrange(5,10)

print(rand_num+total_int)