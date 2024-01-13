"""

One of the significant advantages of object-oriented programming is code reuse, and one way to achieve this is through inheritance. 
Inheritance involves creating a base class or parent class, followed by creating subclasses or child classes using the syntax class ChildClassName(ParentClassName). 
This way, the subclass can inherit the existing attributes and methods from the parent class, a phenomenon known as class inheritance.

Consider another example: both buses and cars are vehicles on the road and share attributes like colour and brand. 
However, buses have a specific attribute, route, and cars have another specific attribute, rego. 
In this case, we can define a parent class, RoadVehicle, and two subclasses, Bus and Car.

"""

# Create parent class, RoadVehicle
class RoadVehicle:

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def detect(self):
        # print vehicle info
        print('Color: "{}" Brand: "{}"'.format(self.color, self.brand), end=" ")


# Create child class, Bus
class Bus(RoadVehicle):

    def __init__(self, color, brand, route):
        RoadVehicle.__init__(self, color, brand) # use parent class to initiate
        self.route = route

    # re-write
    def detect(self):
        RoadVehicle.detect(self)
        print('Route: {}'.format(self.route))


# Create child class, Car
class Car(RoadVehicle):

    def __init__(self, color, brand, rego):
        RoadVehicle.__init__(self, color, brand)
        self.rego = rego

    def detect(self):
        RoadVehicle.detect(self)
        print('Rego: {}'.format(self.rego))


bus1 = Bus("Black", "Benz", "No.56")
car1 = Car("White", "Ford", "YJR37Y")

bus1.detect()  # print Color: "Black" Brand: "Benz" Route: No.56
car1.detect()  # print Color: "Mary" Brand: "Ford" Rego: YJR37Y

"""
In this example, Bus and Car are subclasses of RoadVehicle. 
They inherit the detect method from the parent class, and each subclass has its additional attributes and methods.

In the provided code, did you notice the following points?

1. During the creation of a subclass, you need to manually call the constructor of the parent class (__init__) to complete the construction of the subclass.

2. When calling a method from the parent class within the subclass, you need to prefix it with the parent class's name and include the self parameter. 
    For example, RoadVehicle.detect(self). This can be simplified using the super keyword.
    
3. If a subclass calls a method or attribute, Python first looks for it in the subclass. If found, it is directly invoked; 
    otherwise, Python searches in the parent class. This mechanism facilitates method overriding.
    
In practical Python programming, a subclass can inherit from multiple parent classes (multiple inheritance), and the principle remains the same. 
The first step always involves manually calling the __init__ constructor.

"""


"""

The super() keyword can be used in a subclass to directly invoke the corresponding method from the parent class, simplifying the code. 
In the example below, the Car subclass calls the detect() method from the parent class using super().detect(), which is equivalent to RoadVehicle.detect(self). 
When using the super() keyword to call a method from the parent class in Python, it's important to omit the self parameter within the parentheses.

"""

# Create child class, Car
class Car(RoadVehicle):

    def __init__(self, color, brand, rego):
        RoadVehicle.__init__(self, color, brand)
        self.rego = rego

    def detect(self):
        super().tell() # == RoadVehicle.detect(self)
        print('Rego: {}'.format(self.rego))
