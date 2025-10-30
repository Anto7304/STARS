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