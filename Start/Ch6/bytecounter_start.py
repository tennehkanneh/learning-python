import os
from os import path

def file_info(folder):
  total_bytecount = 0
  
  dirlist = os.listdir(folder)
  print(f"{folder}\n")

  for file in dirlist :
    print(file)
    filepath = folder + "/" + file
    temp_bytecount = 0
     
    if path.isfile(filepath) and file.endswith(".py") :
      temp_bytecount = os.path.getsize(filepath)

      print(f"Byte Count: {temp_bytecount}\n")

    total_bytecount += temp_bytecount

  return print(f"Total byte count of {folder}: {total_bytecount}\n")

file_info("/workspaces/learning-python/Start/Ch6")

file_info("/workspaces/learning-python/Start/Ch7")