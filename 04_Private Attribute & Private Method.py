"""

Private attributes and methods in a class are denoted by a double underscore (__). 

These private attributes or methods cannot be accessed or directly used from outside the class. 

Let's explore this concept using the example of a Car class by making the "make" attribute private.

"""

# Create a class called Car
class Car:

  # Define the car's attributes, initialise the method
  def __init__(self, color, make):
    self.color = color
    self.__make = make
  # Define the method to print car's information
  def show(self):
    print("Color: {}. Make: {}".format(self.color, self.make))

# instantiate object
car1 = Car("Black", 2007)

car1.show() # print Color: Black, Make 2007
car1.__make # print error, this attribute cannot be accessed from outside the class.

"""
If you change "make" to "__make", you can no longer directly access the car's make using car1.__make. 
However, the show() method can still display the make because it is a function within the class and can access private variables.

The same principle applies to private methods. 
If we make show() into __show(), you can no longer print the car's colour and make using car1.__show(). 
It's important to note that private methods must have the self parameter as the first parameter.

In object-oriented programming, it is common to restrict direct access to a class's internal attributes and methods from external classes. 
Instead, external classes are provided with methods to access the internal members, ensuring the security of the program. 
This concept is known as encapsulation.

"""

