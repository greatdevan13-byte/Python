python={"Rajesh","Sumesh","Ramesh","Mahesh","Suneesh"}
data_science={"Rajesh","Sudheesh","Ramesh","Ragesh"}
python.add("John")
data_science.remove("Rajesh")
intersection_course=python.intersection(data_science)
print(intersection_course)

c=python.difference(data_science)
print(c)

combined_list=python.union(data_science)
print(combined_list)

dictionary={
    "python": len(python),
    "data science":len(data_science)
}
for x,y in dictionary.items():
 print("Course :", x ,",","Students :", y)

