mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# print all values 
print(mytuple)

# access indexed values
print(mytuple[0])

# Negative indexing
print(mytuple[-1])

# range of indexing
print(mytuple[0:2])

# length of tuple
print(len(mytuple))

# create tuple with one element
fruit1 = ("apple")    # type str
fruit2 = ("apple",)    # type tuple
print(type(fruit1))
print(type(fruit2))

# tuples are imutables
mytuple = ("apple", "banana", "cherry")
# mytuple[0] = "orange" # you can not change tuples values directly


# first convert tuple into list then change values
tuple_lst  = list(mytuple)
tuple_lst[0] = "Orange"

mytuple = tuple(tuple_lst)
print(mytuple)

# unpack tuple
fruits = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = fruits
print(fruit1, fruit2, fruit3)

# loop in tuples 
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# loop through index
for x in range(len(fruits)):
    print(fruits[x])

# with while loop
fruits = ("apple", "banana", "cherry")
i = 0
while i < len(fruits):
  print(fruits[i])
  i += 1


# join tuples
fruits1 = ("apple", "banana", "cherry")
fruits2 = ("orange", "mango")
fruits = fruits1 +fruits2
print(fruits)

# Count elements in tuples
print(fruits.count("apple"))

# ================== Exercise =============
