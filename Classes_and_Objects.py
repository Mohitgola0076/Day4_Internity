''' 
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
'''

          # 1.) The __init__() Function 
          
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


          # 2.) Object Methods
          
# Insert a function that prints a greeting, and execute it on the p1 object: 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

          # 3.)  The self Parameter
          
 # Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
          
          # 4.)  Modify Object Properties
          
# Set the age of p1 to 40:
p1.age = 40

          # 5.)  Delete Object Properties
          
# we can delete properties on objects by using the del keyword:
# Delete the age property from the p1 object:
del p1.age

          # 6.) Delete Objects
 
# Delete the p1 object:
del p1
