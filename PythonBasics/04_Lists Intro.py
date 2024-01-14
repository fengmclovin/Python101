a = [1, 2, 3]
print(a)

a.append(4)
print(a)

a.append("Five")
print(a)

a.append([6, 7])
print(a)

a.pop()
print(a)

a.pop()
print(a)

print(a[0])
print(a[3])

a[0] = "One"
print(a)

b = ["AAA", "BBB", "CCC"]
print(b)

temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

# or 
b[0], b[2] = b[2], b[0]
print(b)
