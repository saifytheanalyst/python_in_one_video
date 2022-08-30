myset1 = {"apple", "banana", "cherry"}
print(type(myset1))

 # set will remove duplicates automatically
myset2 = {"apple", "banana", "cherry", "apple"}
print(myset2) 


# print all values 
print(myset1)

# access set values
for x in myset1:
    print(x)

# add new element in set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# merge two different sets
fruits = {"apple", "banana", "cherry"}
new_fruits = {"pineapple", "mango", "papaya", "apple"}
fruits.update(new_fruits)
print(fruits)

# merge list into sets
fruits = {"apple", "banana", "cherry"}
new_fruits = ["pineapple", "mango", "papaya", "apple"]
fruits.update(new_fruits)
print(fruits)


# remove items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# remove items with discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# remove last item
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

# clear sets
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# delete set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)


# ================== Exercise ===============
