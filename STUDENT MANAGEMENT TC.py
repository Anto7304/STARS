# STUDENT MANAGEMENT TRACKER 
# LIST to hold all student records

students = []
# function to add new students
def add_student():
    print("\n ---Add New student-----")
    name = input("Enter Student name")
    age = int(input("Enter age"))
    course = input(" Enter Course")

# tuple for fixed data 
info = tuple([name, age])

#dictionary for storing subject marks 
marks = {}
subjects = int(input("Enter the number of subjects: "))

# loop for collecting the marks 
for i in range(subjects):
    subject = input(f"Enter subject {i+1} name: ")
    scores = int(input(f"enter {subject} marks: "))
    marks[subject] = score

# combining data to one dictionary
student = {"info": info, "course": course, "marks": marks}
students.append(student)
print("{name} added successfully!!")

# function to display all students 
def display_students():
    print("\n----- ALL STUDENTS -----")
    if not students:
        print("No students are available")
    else:
        for i, student in enumarate(students, 1):
            name, age = student["info"]
            print(f"{i}. {name} {age} yrs) - {student["course"]}")
            for sub, marks in student["marks"].items()
            print(f"  {sub}: {marks}")

            


