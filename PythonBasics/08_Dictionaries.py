d = {}
# d = {"Feng": 24, "Tian": 30}
# keys are commonly strings or numbers

d["Feng"] = 24
d["Tian"] = 30
d["Lance"] = 16

print(d["Feng"])
print(d["Tian"])
print(d["Lance"])

# print(d["Jayce"])

print(d["Lance"]) # print 16
d["Lance"] = 22
print(d["Lance"]) # print 22

# Example 1
d[10] = 100
print(d[10])

# Iterate over key-value pairs?
for key, value in d.items():
  print(f"Key: {key}; Value: {value}")
