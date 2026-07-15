# Priority queue serves an element according to its priority status (e.g. hospitals, emergency systems)
import heapq

hospital=[]

# Insertion
heapq.heappush(hospital, (3, "High Fever"))
heapq.heappush(hospital, (1, "Heart attack"))
heapq.heappush(hospital, (2, "Fracture"))

# Displaying priority queue
print(hospital)

# Serving higher priority cases first
heapq.heappop(hospital)

# Displaying remaining cases
print(hospital)