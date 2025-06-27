# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)

# hello_func() #calling the function

# function that takes parameters
# def hello_func(greeting):
#   print("hello world!")
#   name = input("What is your name? ")
#   print(greeting, name)

# hello_func("How are you doing")
# hello_func("Hey what is up")


# function that returns a value
def cube(x):
  return x * x * x

result = cube(3)
print(result)

# function with default value for an parameter
def hello_func(greeting, name = None):
  print("Hello World!")
  if name == None:
    name = input("What is your name? ")
  print(greeting, name)

hello_func("Nice to meet you!", "Tenneh")
hello_func(name="John", greeting="What is up")

# function with variable number of parameters
def multi_add(start,* args):
  result = start
  for x in args:
    result = result + x
  return result
  
print(multi_add(10, 4, 5, 10, 4, 10))