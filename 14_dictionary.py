# Creating dictionary
thisdict = {
  "Name": "Saif",
  "Age": 21,
  "profession": "data science"
}
print(thisdict)

# Passing list in dictionary
thisdict = {
  "Name": "Saif",
  "Age": 21,
  "profession": "data science",
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))

# Access element from dictionary
print(thisdict["colors"])

# acess elements usinhg get function
print(thisdict.get("colors"))

# get all keys
print(thisdict.keys())

# get all values
print(thisdict.values())

# get all keys and values
print(thisdict.items())

# Add new element in dictionary
car = {
"brand": "Tesla",
"model": "2022",
}
car["color"] = "red"
print(car)

# Check if Key Exists
if "color" in car:
    print("Yes, 'color' is one of the keys in the dictionary")

# change values in dictionary
car["color"]="blue"
print(car)


# delete item from dictionary
print(car.pop("color"))
print(car)

# delete last inserted item from dictionary
car.popitem()
print(car)


# clear dictionary
car.clear()
print(car)


# looping dictioary
car = {
"brand": "Tesla",
"model": "2022",
"color" : "red"
}

for x in car:
    print(x, car[x]) # this will return keys

# getting keys from dictionary
for key in car.keys():
    print(key)


# getting values from dictionary
for value in car.values():
    print(value)

# getting keys and values
for key, value in car.items():
    print(key, value)

# dictioanry comprehension
{print(x) for x in car}

# copy dictionary
car2 = car.copy()
print(car2)


# create Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "shazia",
    "year" : 2004
  },
  "child2" : {
    "name" : "Rani",
    "year" : 2007
  },
  "child3" : {
    "name" : "shabana",
    "year" : 2011
  }
}

print(myfamily)
# get specific child values
print(myfamily["child1"])

# check all the function used for dictionary
print(dir(myfamily))


# ============ Exercise ================

