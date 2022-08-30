# Lists are used to store multiple items in a single variable.

# creating list method 1
from ast import comprehension

from pyparsing import condition_as_parse_action


mylist = ["apple", "banana", "cherry"]
mylist = ["apple", "cherry","banana", 1,2,3,4,2.5]
print(mylist)

# creating list method 2
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# check type
print(type(mylist))

# check length
print(len(mylist))

# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items at specific index 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Add List Items using append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# change value on existing one
thislist[1] = "orange"

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Sort Lists
# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


#================== Loop Through a List ===============

# for loop

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# ============ Looping Using List Comprehension ===========

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# list comprehension with specific condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
[print(x.upper()) for x in fruits if "a" in x]
