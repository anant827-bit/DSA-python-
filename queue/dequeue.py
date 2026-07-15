# Double Ended Queue -- Dequeue
from collections import deque
d_queue= deque()

# Insertion
d_queue.append("Divyansh")
d_queue.append("You")
d_queue.append("Vaibhavi")

# Display queue after insertion
print(d_queue)

# Deletion
print("Deleted Element:", d_queue.popleft())

# Display queue after deletion
print(d_queue)

# Length of queue
print("Length of queue:", len(d_queue))

# Check if queue is empty
print("Is queue empty?", len(d_queue)==0)
