dict = {"name" : "Ankit" ,
         "Course" : "CE" ,
           "makrks" : 98}

# mehthods
dict["hobby"] = "bike riding"
print(dict)

dict["hobby"] = "cooking"

print(dict)

del dict["hobby"]

course = dict.pop("Course") #return value

print(course)

dict.popitem()
print(dict)

dict.clear()


d = {"a": 1, "b": 2}
for key in d:
    print(key)

d = {"a": 1, "b": 2}
for value in d.values():
    print(value)