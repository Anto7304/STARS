"""
student management system

list
create a list  and give it some student names.
we apppend some student and extend
we remove students
we access a student by index


sets - managing courses

create a set to store courses
add a course
try to add a duplicate and print and see the results
check if course exist in the set


tuples-timetable
create a course tuple
access tuple
try to change a tuple


dictionary


"""


print("Student Management System")
print("-"*40)

student_list = ["Newton","Barbra","Peter"]
#print(student_list)

#adding alex in list 

student_list.append("alex")
#print(student_list)

#adding hezron at index 2
student_list.insert(1,"Hezron")
#print(student_list)


#remove newton 
#print(student_list[0])
student_list.remove("Newton")

#print(student_list)

#clearing list
student_list.clear()
#print(student_list)

del student_list
#print(student_list)


#tuples

mytuple=("item1","item2","item3")
"""
ordered/indexed
adds item to existing list .extend()
immutable- they cannot be added or changed

"""

#print(mytuple[2])#indexed

#mytuple[2]="item9"
#print(mytuple)

list=[]
list.extend(mytuple)

#print(list)

list[2]="item9"
#print(list)

items=tuple(list)
#print(items)

#sets

"""
it is not ordered
does not store duplicates
"""

sets={1,2,3,4,4,5,5,6,7,8}#doesn't allow duplicates
#print(sets)

courses={"Maths","Chemistry","Cre","Biology"}
#print(courses)

#adding item in set
courses.add("Computer")
#print(courses)

courses.remove("Chemistry")
#print(courses)



courses.pop()
#print(courses)
courses.discard("Maths")
#print(courses)


courses.clear()
#print(courses)

#dictionary
items={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}


#print(items["key2"])
for key,value in items.items():
    print(f"{key}: {value}")








