# LinkedIn Learning Python course by Joe Marini
# Example file for using built-in functions
#

mystring = "The quick, brown fox jumped over the lazy dog!"
mynumbers = [1,3,5,6,9,12,14,17,20,30]

# the len() function calculates the length of a sequence
# print(len(mystring))
# print(len(mynumbers))

# the max() and min() functions will find the largest and smallest value in a sequence
# print(max(mystring))
# print(min(mystring))

# print(max(mynumbers))
# print(min(mynumbers))

# the str() function will return a string version of an object
prefix = "result: "
result = 5

print(prefix + str(result)) # can only concatenate a str with a str

print(prefix + str(3.1415))
# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops 
for i in range(5, 15, 2): #ending value is outside of range (i.e i > 15); by 2s
  print(i)

for i in range(5, len(mystring), 2) :
  print(mystring[i])

# the print function itself is pretty flexible - you can embed variables directly in it
greeting = "Hello!"
count = 10

print(f"{greeting} you are visitor number {count}") 
