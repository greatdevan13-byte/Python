attendance = [18, 20, 19, 15, 21]
Total_attendance=0
count=0
for x in attendance:
    Total_attendance+=x
    if x>=20:
        print("Full")
        count+=1
    else:
        print("Not full")
       
print("Total count :",count)   
print("Total attendance :",Total_attendance)    
  
             

               