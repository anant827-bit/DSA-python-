arr=[1,2,3,4,5]

# method-1
for i in range(len(arr)):
    print(arr[i], end=" ")
print()

# method-2
for i in arr:
    print(i, end=" ")
print()

# reverse traversal - method 1
for i in reversed(arr):
    print(i, end=" ")
print()

# reverse traversal - method 2
for i in arr[::-1]:
    print(i, end=" ")
print()

# reverse traversal - method 3
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")