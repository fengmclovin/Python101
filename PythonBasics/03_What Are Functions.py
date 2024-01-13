# A collection of instructions
# A collection of code

def function1():
    print("Hello, World")
    print("G-day, Mate")
print("This is outside the function")

# A mapping
# Input or an argument

def function2(x):
    return 2*x
    
a = function2(3) # return value pr output
print(a)
b = function2(4)
print(b)
c = function2(5)
print(c)

# d = function2()
# TypeError: function2() missing 1 required positional argument: 'x'

def function3(x, y):
    return x + y

e = function3(1, 2)
print(e)

def function4(x):
    print(x)
    print("Still in function4")
    return 3*x

f = function4(4) #4 / Still in function4
print(f) # 12

def function5(some argument):
    print(some argument)
    print("Thank you")

function5(4) # 4/ Thank you

# BMI Calculator
name1 = "Feng"
height_m1 = 1.7
weight_kg1 =75

name2 = "Tian"
height_m2 = 1.8
weight_kg2 = 80

name3 = "Lance"
height_m3 = 1.83
weight_kg3 = 90

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print(f"bmi: {round(bmi)}")
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
        
result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result)

# Miles to Kilometers Conversion
# km = 1.6 miles

def convert(miles):
    return 1.6 * miles

print(convert(8))
