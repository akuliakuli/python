students = []


def get_name(student):
    return student["name"]

with open("names.csv") as file:
    for line in file:
        name,school = line.rstrip().title().split(",")
        student = {"name":name, "school":school}
        students.append(student)


for student in sorted(students,key=lambda student:student['name']):  
    print(f"{student}")