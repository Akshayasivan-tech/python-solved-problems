students={"Arun": 85, "Bala": 90, "Chitra": 78, "Divya": 92}
highest=max(students,key=students.get)
print("Highest marks scored by:",highest,"with marks:",students[highest])
print("Mark:",students[highest])