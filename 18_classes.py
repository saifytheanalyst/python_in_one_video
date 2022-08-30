
# create class
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# __init__ is constructor which is automatically called when we create object of class
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

p1 = Person1("saif",21)
print(p1.name)
print(p1.age)


# creating class with out constructor
class Person2:
    def address(self, add):
        self.addr = add
        print(add)

p2 = Person2()
p2.address("karachi")


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def my_data(add):
    print("Hello my name is " + add.name)

p3 = Person("saif", 21)
p3.my_data()
