students={"Arun": 85, "Bala": 90, "Chitra": 78, "Divya": 92}
sorted_dict=dict(sorted(students.items(),key=lambda x:x[1]))
print(sorted_dict)