# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)

# Operators are used to perform operations on variables
# print(myint + myfloat)
# print(myint + myfloat)
# print(myint / myfloat)
# print(myint % 3)

another_str = " This is another string"
print(mystr + another_str)

print("nom " * 3)

# Logical and comparison operators 
print(myint == 10)
print(myint != 20)
print(myint > 20)
print(myfloat < 10)

print(myint < 5 and myfloat < 25)
print(myint < 5 or myfloat < 25)
print(not(myint < 5 or myfloat < 25))

# re-declaring a variable works
myint = "abc"
print(myint)