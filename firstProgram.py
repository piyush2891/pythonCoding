print("Hello World")
print("1"+'1'+'11')
print(23, "11")
print(23+11)
name = "Piyush"
age = 33
price = 3333.12
print(name,age,price)
print(type(name))
print(type(age))
print(type(price))

age = 23
old = False
a = None
print(type(old))
print(type(a))

# Type conversion example
# automatic conversion which python will do for us

ab = 2
cd = 4.25
sum = ab+cd # 2.0 + 4.25 = 6.25
print(sum)

# type casting, manually we have to do this otherwise we will get an error
""""""
# a ="2"
# b =4.25
# sum = a+b
# print(sum)
""""""
#  TypeError: can only concatenate str (not "float") to str
# to solve this we can follow
a =int("2")
b =4.25
sum = a+b
print(sum)

name = input("enter your name")
print("Welcome",name)

# when we take an input using 'input' keyword it takes as a string

# write a program to take 2 numbers as input and print their sum

firstNo = int(input("Enter first number"))
secondNo = int(input("Enter second number"))
sum = firstNo + secondNo
print(type(sum),sum)


# WAP to input side of a sqaure & print its area

side = float(input("Enter length of sqaure"))
area = side * side
print("sqaure area is:",area)

# WAP to print True if a is greater than or equal to b. If not print False

a = 22
b = 10
print(a>=b)