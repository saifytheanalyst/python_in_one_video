# single line string
a = "Hello"
print(a)

# Multiple line strings in double quotation mark
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Multiple line strings in single quotation mark
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# acessing element with index
a = "Hello, World!"
print(a[1])

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

# ====================== String Slicing ==================

# String slicing
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# ====================== String Modification ==================

# Upper case
a = "Hello, World!"
print(a.upper())

# lower case
a = "Hello, World!"
print(a.lower())

# title case
a = "hello world!"
print(a.title())

# Remove Whitespace
a = "          Hello, World!            "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# count character in string
print(a.count('l'))

# ====================== String Concatenation ==================

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# ====================== String formating and f strings ==================

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

age = 36
txt = "My name is John, and I am {}".format(age)
print(txt)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print(f"I want to pay {quantity} dollars for {itemno} pieces of item {price}.")

# ====================== Escape Character ==================

# An escape character is a backslash \ followed by the character you want to insert.

# example 
# We are the so-called "Vikings" from the north.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# for single quotation
txt = "We are the so-called \'Vikings\' from the north."
print(txt)

# for new line
txt = "We are the so-called Vikings\n from the north."
print(txt)

# ====================== Exercise ==================
