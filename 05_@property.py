"""

The use of @property provides an interesting and powerful aspect. 
In the mentioned case, users cannot access the car's make using car1.__make. 
However, if we want users to access the make using car1.make while still keeping it as a private variable __make, we can utilize Python's @property decorator. 
This involves defining a method (make() in this case) and using @property to disguise this function as an attribute.

"""

# Create a class called Car
class Car:

  # Define car's attributes, initialise the method
  def __init__(self, color, make):
    self.color = color
    self.__make = make
  # Define the method to print car's information

  # using @property to disguise this function as an attribute.
  @property 
  def make(self):
    print(f"Color: {self.color}. Make: {self.__make}")

# instantiate object
car1 = Car("Black", 2007)

car1.make # print Color: Black. Make: 2007

"""

It's important to note that once a function is decorated with @property, 
you can call the function without using parentheses, 
making it appear as if you are accessing an attribute directly.

"""
