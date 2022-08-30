# A function is a block of code which only runs when it is called.


# Creating a Function
from email.headerregistry import Address


def my_function():
    print("Welcome to Data Sience with Saify")

# calling function
my_function()
my_function()


# passing arguments
def my_car(car_name):
  print(f"i purchased {car_name} car")

my_car("Ferari")
my_car("Tesla")

# pass more arguments
def address_book(f_name, l_name, age):
    print(f"My name is {f_name} {l_name} i am {age} years old")

# calling function
address_book("saif","ali",21)

# if you don't know the number of arguments
def new_addrss_book(**kwargs):
    print("My name is {} and i am {} years old ".format(kwargs["fname"], kwargs["age"]))
new_addrss_book(fname="saif", age=21)


# pass statement
def my_courses():
    pass
my_courses()

# Even Numbers
def even_numbers(destination):
    for i in range(1,destination):
        if i%2==0:
            print(i, end=" ")
even_numbers(20)
even_numbers(50)


# ================== Exercise ==================

# print Odd number from 1-50 using function
