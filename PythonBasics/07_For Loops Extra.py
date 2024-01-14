# Example 1
a = ["AAA", "BBB", "CCC"]
for element in a:
  print(element)

for i in range(len(a)): # 0, 1, 2
  for j in range(i + 1):
    print(a[i])

# i = 0 -> j = 0
# i = 1 -> j = 0, 1
# i = 2 -> j = 0, 1, 2

"""
The outer loop (for i in range(len(a))) iterates over each index of the list a.

The inner loop (for j in range(i + 1)) iterates from 0 to the current index i in the outer loop.

Inside the inner loop, print(a[i]) is executed, which prints the element at index i of the list a.

Now, let's see how the loops iterate:

When i is 0:
Inner loop (for j in range(i + 1)) runs once with j being 0.
Prints "AAA".
When i is 1:
Inner loop runs twice with j being 0 and 1.
Prints "BBB" twice.
When i is 2:
Inner loop runs three times with j being 0, 1, and 2.
Prints "CCC" three times.

"""
