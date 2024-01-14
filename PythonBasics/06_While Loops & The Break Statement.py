# Example 1
total = 0
for i in range(1, 5):
    total += i
print(total)

# Example 2
total2 = 0 
j = 1
while j < 5:
  total2 += j
  j += 1

print(total2)

# Example 3
given_list = [5, 4, 3, 2, 1]

total3 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
  total3 += given_list[i]
  i += 1

print(total3)

# Example 4
given_list2 = [5, 4, 3, 2, 1, -2, -3, -4]
total4 = 0
for element in given_list2:
    if element <= 0:
        break
    total4 += element
print(total4)

# Example 5
# given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total5 = 0
i = 0
while True:
    total5 += given_list2[i]
    i += 1
    if given_list2[i] <= 0:
        break
print(total5)

# While loop is used to execute a block of code repeatedly until given boolean condition evaluated to False. 
# If we write while True then the loop will run forever.
