# Basic Operations on Array
arr = [1,2,3,4,5]

# Insertion at end
arr.append(6) 
print(arr)

# Insertion at position
arr.insert(2,10)
print(arr)

# Deletion at end
arr.pop()
print(arr)

# Deletion at position - method 1
arr.pop(2)
print(arr)

# Deletion at position - method 2
del arr[3]
print(arr)

# Deletion by value
arr.remove(3)
print(arr)

# Slicing
print(arr[1:3])