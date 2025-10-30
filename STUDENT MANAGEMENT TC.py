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
    info = (name, age)

    #dictionary for storing subject marks 
    marks = {}
    subjects = int(input("Enter the number of subjects: "))

    # loop for collecting the marks 
    for i in range(subjects):
        subject = input(f"Enter subject {i+1} name: ")
        score = int(input(f"enter {subject} marks: "))
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
            for sub, marks in student["marks"].items():
                print(f"  {sub}: {marks}")

# funtction to show us the top performer 
def top_performer():
    print("\n---- TOP PERFORMER ----")
    if not students :
        print ("No Student Records have been added yet!!")
        return

    top_student = None
    top_avg = 0
# shukran
    for student in students:
        marks = student["marks"].values()
        avg = sum(marks) / len(marks)
        if avg > top_avg:
            top_avg = avg
            top_student = student
        
    name. _ = top_student["info"]
    print(f" TOP PERFORMER: {name} with average (top_avg:.2f)")

    # Tunataka tutrack unique courses: so hapa tutatumia sets
    course = set()

    '''
     finally tunaunda menu ya ku allow the user a view students, 
     add students ama pia kucheck top performer and finally ku exit
     tutatumia while loop
     '''


    while True:
        # mennu 
        print(" ----- STUDENT MANAGEMENT SYSTEM -----")
        print("1. Add a Student")
        print("2. View Students ")
        print("3. Show Top Performer")
        print("4. Exit")

        # we fetch the input from the user for any of the choices atachagua
        choice = input("Enter Choice: ")
# hizi ni call functions
        if choice == "1":
            add_student()
            courses.add(students[-1]["course"])
        elif choice == "2":
            display_students()
        elif choice == "3":
            top_performer()
        elif choice == "4":
            print(f"\nUnique courses: {courses}")# hapa nili intergrate na AI
            print("Goodbye.....exiting")
            break
        else: 
            print("INVALID CHOICE!!!, try again.")




