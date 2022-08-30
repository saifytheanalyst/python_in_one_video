from cv2 import inRange


print(1)
print(2)
print(3)
print(4)
print(5)


for x in range(5):
    print(x)


for x in range(1,5):
    print(x)



for x in range(1,10,2):
    print(x, end=" ")

# if Else in For Loop
for x in range(6):
  if x == 3:
    print(x)
else:
  print("Finally finished!")


# Nested Loops
for x in range(1,6):
  for y in range(1,3):
    print(x, y)

# pass statement
for x in range(10):
  pass