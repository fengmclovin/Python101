"""
Similar to how certain variables belong to a class and certain methods are class-specific rather than specific to individual objects, 
it's important to note that methods associated with objects have a self parameter, 
such as __init__(self) and show(self). The self parameter refers to the object itself. 

On the other hand, methods associated with a class don't use self but use cls as a parameter, representing the class itself. 
Additionally, it's common practice to use the @classmethod decorator to indicate class methods.

Taking the example of the Car class, 
suppose we want to print the number of car objects created without using the print function directly 
but by defining a class method for this purpose. We can do it like this:

"""

class Car:

    # number here is a class variable, defined outside a method, hence, it's not an instance variable.
    number = 0

    # Define Car attributes， initialize the method
    # colour & make instance variables defined within the method.
    def __init__(self, color, make):
        self.color = color
        self.make = make
        Car.number = Car.number + 1

    # Define the method to print the car's info
    def show(self):
        print(f"Name: {self.color} Score: {self.make}")

    # Define the class method, print car number
    @classmethod
    def total(cls):
        print(f"Total: {cls.number}")


# instantiate object
car1 = Car("Black", 2007)
car2 = Car("White", 2014)
car3 = Car("Red", 2013)

Car.total()  # print Total: 3

