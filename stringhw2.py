para="""Python is an interpreted, high-level and general-purpose programming language.
      Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
      Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects"""
para_length=len(para)
print(para_length)
first_character=para[0]
second_character=para[-1]
print("First character:",first_character )
print("Last character:",second_character )
sliced_character=para[0:50]
print("Sliced characters:",sliced_character)
Replaced_character=para.replace("Python","PYTHON")
print("Replaced string:",Replaced_character)
lowercase_character=para.lower()
print("\tLowercased string:" ,lowercase_character)
Space_cancellation=para.strip()
print(Space_cancellation)
Splitted_string=para.split(" ")
print("Splitted string:",Splitted_string)
print("Course" in para)
print("The course description is {} characters long and has {} words.".format(para_length,len(Splitted_string)) )
