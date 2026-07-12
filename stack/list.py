# Stack using List
stack=[]

# Insertion
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)

# Deletion
del_element=stack.pop()
print("Popped Element:", del_element)

# Check if stack is empty
print("Stack is empty?", len(stack)==0)