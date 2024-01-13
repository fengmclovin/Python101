"""
Class and Object

A Class serves as a blueprint for a group of objects sharing similar attributes and methods, while an Object represents a specific instance of that class. 

For instance, when considering cars with common attributes like colors and makes, a class named "Car" can be designed to encapsulate these attributes, along with customized methods for displaying their colors and makes.

Attributes refer to variables or data within a class that describe the shared characteristics among all objects, such as a car's color and make. 

Methods, on the other hand, are functions within a class that distinguish them from functions outside the class and are employed to execute specific functionalities, like printing out a car's color and make.

Creating a class involves using the "class" keyword. In the case of the Car class, it would be defined to include the necessary attributes and methods for handling student information.

"""

# Create a class called Car
class Car:

  # Define car's attributes, initialise the method
  def __init__(self, color, make):
    self.color = color
    self.make = make
  # Define the method to print car's information
  def show(self):
    print("Color: {}. Make: {}".format(self.color, self.make))

"""
In this scenario, I've merely outlined an abstract class without the computer allocating any storage space. 

Storage space is generated only when the class instantiation (instance) is fully executed, leading to the creation of a specific object. 

Therefore, an object is essentially an instance of a class.

"""

# To create a specific student object, we need to input:

car1 = Car("Black", 2007)
car2 = Car("White", 2014)

"""
In this case, "Car" is the class, and "car1" and "car2" are the concrete student objects I've instantiated. When I input the above code, Python automatically invokes the default __init__ constructor to generate specific objects. 

The keyword "self" is a crucial parameter, representing the created object itself.

Once you've created specific objects, you can directly access the car's color and make using car1.color and car1.make, respectively. 

Additionally, you can print the car's color and make directly by calling car1.show().

"""

