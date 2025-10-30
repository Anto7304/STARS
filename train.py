#print("student management system")
#print("_"*40)

student_list = ["newton", "barbra", "peter", "David"]
#print(student_list)
#adding john in list
student_list.append("john")
#print(student_list)
#adding hezron at index 2
student_list.insert(2, "hezron")
#print(student_list)
#REMOVE newton from list
student_list.remove("newton")
#print(student_list)
#clearing list
student_list.clear()
#print(student_list)

#tuples
mytuple=("item 1", "item 2", "item 3")

"""
odered/indexed
adds item to existing list
immutable/cannot be added or changed
allows duplicate items
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
not ordered
does not store dublicate
"""

sets={1,2,3,4,5,6,7,8}
#print(sets)
courses={"maths", "biology", "history", "maths"}
#print(courses)

#adding an item in set
courses.add("computer")
#print(courses)

courses.clear()
#print(courses)

#courses.pop()
#print(courses)

courses.discard("maths")
#print(courses)  

courses.clear()
#print(courses)


#dictionaries
item={
"key1":"value1",
"key2":"value2",

"key3":"value3",

"key4":"value4",

}
print(item)

#print(item["key2"])#accessing value using key   
#
for key,value in item.items():
 print(key,value)      
