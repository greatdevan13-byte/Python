frontend={"Hari","Ramu","Somu","Venu"}
backend={"Ramu","Sasi","Meena"}
backend.add("Leela")
frontend.remove("Venu")

intersected_courses=frontend.intersection(backend)
print(intersected_courses)

only_backend=backend.difference(frontend)
print(only_backend)

combined_students=frontend.union(backend)
print(combined_students)

courses={
    "Frontend": len(frontend),
    "Backend": len(backend)
}

for x,y in courses.items():
    print("Courses :",x, ",", "Students :",y)
