# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 100,100 #declaring two variables on to the same line


# conditional flow uses if, elif, else
if x < y: 
  print("x is less than y")
elif x > y :
  print("x is greater than y")
else: 
  print("x and y are the same")

# conditional statements let you use "a if C else b"
result = "x is less than y" if (x < y) else "x is greater or equalt to y"
print(result)