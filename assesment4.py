# #1 create a tuple with five numbers
# tuple=(12,45,43,56,33)
# print(tuple)

# #2 acess the third element in a tuple 
# number=(23,54,35,65,12)
# num=number[2]
# print(num)

# #3 unpack a tuple in to seprate variable
# name =("apple","orange","kiwi")
# (red,orng,black) = name

# print(black)

# #4 add a new fruit to the set
# fruits={"apple","orange","dragon fruit","banana","grap"}
# fruits.add("gwawa",)
# print(fruits)

# #5 remove an element from a set
# car={"swift","punch","odiee","bmw","mustang"}
# car.remove("punch")
# print(car)

# #6 Find union of two sets
# A={12,23,34,54,56}
# B={12,54,34,36,21}
# result=A.union(B)
# print(result)

# #7 find intersection of two sets
# x={34,87,45,23,21,12}
# y={21,54,34,43,50,12}
# result=x.intersection(y)
# print(result)

# #8 check if one set is sub set of another
# P={12,43,54,65,23}
# Q={12,45,54,43,32,76}
# result=P.__sub__(Q)
# print(result)

# #9 convert a list with duplicate values in to a set to remove duplicate
# list=[10,20,32,43,45]
# result=set(list)
# print(result)

# #10 create a dictonary storing student names and marks
# students={"Deep":65,"jayesh":43,"yash":70,"kavan":60}

# print(students)

# #11 add a key-value pair to an existing dictnory
# students={"Deep":65,"jayesh":43,"yash":70,"kavan":60}
# x={"parth":76}
# students.update(x)
# print(students)

# #12 Delete a key-value pair from a dictnory
# students={"Deep":65,"jayesh":43,"yash":70,"kavan":60,"parth":76}
# students.pop("jayesh")
# print(students)

# #13 merge two dictnory into one 
# class_1= {"jayesh":43,"Deep":57,"yash":55}
# class_2={"rutvik":56,"mayank":76,"rudra":60}

# class_1.update(class_2)
# print(class_1)

# #14 check if a key exist in a dictnory
# key={10,34,54,67,76}

# if 34 in key:
#     print("key exist")

# #15 count word frequency in a given string using a dictnory
# string="Python makes data processing and word Python counting straightforward word."
# x=string.split()
# frequency={}
# for i in x:
#     if i not in frequency:
#         frequency[i]=1 
#     else:
#         frequency[i]+=1
# print (frequency)     

# #16 find the key with maximum value in a dictnory
# members={"class1":43,"class2":54,"class3":61,"class4":39}
# result=max(members, key =members.get)
# print(result)

# #17 reverse key and value in a dictnory
# cars={"swift":12,"alto":8,"fronx":10,"harier":5}
# for k,v in reversed(cars.items()):
#     print(k,v)


# #18 update the value for a specific key
# Departments={"civil":48,"computer":70,"electrical":55,"mechanical":39}
# Departments.update({"mechanical":45})
# print(Departments)


# #19 conver a list of tuples into a dictnory
# cars_list = [("swift", 12), ("alto", 8), ("fronx", 10), ("harier", 5)]
# my_dictnory= dict(cars_list)
# print(my_dictnory)
