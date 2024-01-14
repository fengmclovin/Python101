# Example 1
a = ["AAA","BBB", "CCC"]

for element in a:
  print(element)
  print(element*2)

# Example 2
b = [9, 6, 3]
total = 0
for e in b:
  total = total + e

print(total)

# Example 3
# 1, 2, 3, 4
c = list(range(1, 5))
print(c)

# Example 4
total2 = 0
for i in range(1, 5):
  total2 += i

print(total2)

# Example 5 
print(list(range(1, 8)))

# Example 6
print(4 % 3)
print(5 % 3)
print(1 % 3)
print(2 % 3)
print(6 % 3)

# Example 7
total3 = 0
for i in range(1, 8):
  if i % 3 == 0:
    total3 += i

print(total3)

# Example 8
total4 = 0
for i in range(1,100):
  if i % 3 == 0 or i % 5 ==0:
    total4 += i

print(total4)

# List all multiples of 3, 5
# that are less than 100
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
