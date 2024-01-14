class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
    
    def introduce_self(self):
        print(f"My name is {self.name}, My color is {self.color}, and My weight is {self.weight} kg.")

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i
    
    def sit_down(self):
        self.is_sitting = True
    
    def stand_up(self):
        self.is_sitting = False

p1 = Person("Feng", "Aggressive", False)
p2 = Person("Tian", "Talkative", True)

# p1 owns r2
p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
