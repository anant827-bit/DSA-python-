class queue():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    
    def insert(self, item):
        self.items.append(item)

    def delete(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)
    
    def display(self):
        print("Queue(Front -> Back):", self.items)

    def length(self):
        return len(self.items)
    
q1=queue()
# Inserting values in queue
q1.insert(1)
q1.insert(2)
q1.insert(3)

# Displaying queue after insertion
q1.display()

# Deleting element from queue
print("Deleted Item:", q1.delete())

# Displayong queue after deletion
q1.display()

# Finding size of queue
print("Size of queue:", q1.length())

# Checking if queue is empty
print("Is queue empty?", q1.isEmpty())