numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]


def count_numbers(which, numbers):
  count = 0

  for x in numbers:
    if which == "even":
      count = count + 1 if (x % 2) == 0 else  count
        
      
    elif which == "odd":
      count = count + 1 if (x % 2) != 0 else count
      
    else:
      print("Incorrect 'which' parameter count: -1")
      return -1
    
  print("Even count:" if which == "even" else "Odd count:", count)
  return count 
  
    

count_numbers("even", numbers)
count_numbers("odd", numbers)
count_numbers("blarg", numbers)

    


