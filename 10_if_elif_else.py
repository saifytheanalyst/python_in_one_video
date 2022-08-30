a = 33
b = 200
if b > a:
  print("b is greater than a")

# short hand
a = 33
b = 200
if b > a: print("b is greater than a")

a = 33
b = 200
if b > a:
  print("b is greater than a")
if a < b:
    print("Hurrah")

# elif (if first condition is true then it will break)
a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a < b:
    print("Hurrah")

# else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Try if else with logical operators
# with and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# with or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# nested if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# pass statement
a = 33
b = 200
if b > a:
  pass
