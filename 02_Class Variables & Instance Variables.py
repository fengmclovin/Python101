"""
Class Variables & Instance Variables

Assuming we need to add a counter, named "number," to the Car class, such that it automatically increments by 1 every time a new car object is created. 

Since this counter is not specific to any individual car but belongs to the Car class, it is referred to as a class variable. 

On the other hand, the color and make belong to each car object, making them instance variables or object variables.

The updated Car class would look something like this:

"""

# Create a class called car
class Car:

    # number here is a class variable, defined outside a method, hence, it's not an instance variable.
    number = 0

    # Define Car attributes， initialize the method
    # color & make instance variables defined within the method.
    def __init__(self, color, make):
        self.color = color
        self.make = make
        # Can you spot a mistake that has been made here?
        number = number + 1

    # Define the method to print the car's info
    def show(self):
        print(f"Name: {self.color} Score: {self.make}")

"""
The distinction between class variables and instance variables is substantial, and their access methods differ.

Class Variables:

Class variables are shared across all instances of an instantiated object.
They are defined within the class but outside any functions.
The appropriate way to access or invoke a class variable is by using either ClassName.variable_name or self.__class__.variable_name. 
self.__class__ automatically returns the class name for each object.

Instance Variables:

Instance variables are defined within methods and are specific to a particular object.
The correct method for accessing or invoking an instance variable is by using either object_name.variable_name or self.variable_name.

Please note the error in the preceding Car class: 

Attempting to directly use number = number + 1 to modify the class variable number. 
The correct approach is to use Car.number or self.__class__.number to access the class variable. 

The following code illustrates the correct usage:

"""


# Create a class called car
class Car:

    # number is a class variable，and does not belong to any instance
    number = 0

    # Define Car attributes， initialize the method
    # color & make instance variables defined within the method.
    
    def __init__(self, color, make):
        self.color = color
        self.make = make
        Car.number = Car.number + 1

    # Define the method to print the car's info
    def show(self):
        print(f"Name: {self.color} Score: {self.make}")

# instantiate object
car1 = Car("Black", 2007)
car2 = Car("White", 2014)
car3 = Car("Red", 2013)

print(Car.number)  # print 3
print(car1.__class__.number) # print 3
print(car2.__class__.number) # print 3
print(car3.__class__.number) # print 3


"""

In Python, self.__class__ is a way to refer to the class of the current instance within a class method. 
The self parameter is a convention in Python methods that refers to the instance of the class. 
By using self.__class__, you can access the class itself from within a method.

In the __init__ method, self.__class__.number is used to access the class variable number and increment it when a new car is created. 

This way, you ensure that you are modifying the class variable associated with the class itself rather than an instance-specific variable.

"""
