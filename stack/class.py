# Stack using class
class stack():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        popped=self.items.pop()
        return popped
    
    def display(self):
        print("Stack(Top -> Bottom): ", self.items[::-1])

    def length(self):
        return len(self.items)
    
s1 = stack()
# Inserting 1,2,3
s1.push(1)
s1.push(2)
s1.push(3)

# Displaying stack after insertion
s1.display()

# Popping last element
x=s1.pop()
print("Popped element:", x)

# Displaying stack after popping
s1.display()

# Checking if stack is empty
print("Is stack empty?", s1.isEmpty())

# Finding out number of elements in stack
print("Number of elements in stack:", s1.length())