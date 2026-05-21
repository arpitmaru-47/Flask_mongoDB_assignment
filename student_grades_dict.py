students = {
    "appi" : "A",
    "kannu" : "B"
}

# Add new student
students["Arpit"] = "A"

# Update grade
students["kannu"] = "A"

# print all students
for name, grade in students.items():
    print(name, ":", grade)