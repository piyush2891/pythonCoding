# A built-in data type that stores set of values
# list in python [] is mutable, value can be changed


# marks = [12,13,14,15,16,17]
# print(marks)
# print(type(marks))
# print(marks[2])
# print(len(marks))
# we can store diff type of data in a list
# student = ["karan", 85, "Dilli"]
# print(student[2])
# student[2] = "mumbai"
# print(student)
# print(student[6])
# slicing is possible in 

# marks = [87,89,91,93,95]
# print(marks[0:])
# print(marks[:5])
# print(marks[1:2:4])
# print(marks[1:3])
# slicing also possible with negative indexes

# list = [2,1,3]
# list.append(4)  will add the value at last
# print(list)
# list.sort()
# print(list)
# list.sort(reverse = True)
# print(list)
# list.insert(4,5)
# print(list)


# name = ["a", "c", "e", "b", "d"]
# name.sort(reverse=True)  reverse
# print(name)
# name.sort()  ascending order
# print(name)
# name.remove("a") directly remove any element when find first time
# print(name)
# name.pop(0) remove the element at 0 index
# print(name)

# tuple in python () is immutable, value can't be changed

# tup = (1,2,3,4,5)
# print(type(tup))
# print(tup)
# # tup[0] =2 TypeError: 'tuple' object does not support item assignment
# print(tup)
# # tup1 = (1) <class 'int'>
# print(type(tup1))
# # tup2 = (1,) <class 'tuple'>
# print(type(tup2))

# tupp = (1,2,3,4,4,5,)
# print(tupp.index(4))
# print(tupp.count(4))

# WAP to enter three movies and store them in a list
# allmv = []
# mv1 = input("Enter you first fav movie: ")
# mv2 = input("Enter you second fav movie: ")
# mv3 = input("Enter you third fav movie: ")
# allmv.append(mv1)
# allmv.append(mv2)
# allmv.append(mv3)
# print(allmv)
# print(allmv[2])

# palindrome maam, racecar, nitin, 
ele = ["n", "i" ,"t", "i", "n"]
# ele = [1,2,3,2,1,6]
rele = ele.copy();
rele.reverse()
if (ele == rele):
    print("palindrome")
else:
    print("non palindrome")




