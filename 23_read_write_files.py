# # The key function for working with files in Python is the open() function.

# # When you have and want to open in python
# f = open("./demofile.txt","r")
# # print(f.read())

# for x in f:
#     print(x)

# f.close()


# # create file in python
# # f = open("Python.txt",'x')

# f = open("python.txt", "a")
# f.write("Now the file has more content!")
# f.close()


# #open and read the file after the appending:
# f = open("python.txt", "r")
# print(f.read())


# Delete files if exist
import os
if os.path.exists("python.txt"):
  os.remove("python.txt")
else:
  print("The file does not exist")