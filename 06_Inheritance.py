"""

One of the significant advantages of object-oriented programming is code reuse, and one way to achieve this is through inheritance. 
Inheritance involves creating a base class or parent class, followed by creating subclasses or child classes using the syntax class ChildClassName(ParentClassName). 
This way, the subclass can inherit the existing attributes and methods from the parent class, a phenomenon known as class inheritance.

Consider another example: both buses and cars are vehicles on the road and share attributes like color and brand. 
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
