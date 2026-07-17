# Counting frequency of orders in a restaurant
orders=[
    "Dosa", "Idli", "Idli", "Noodles", "Maggie", "Dosa", "Maggie", "Noodles", "Pasta", "Dosa", "Pasta", "Pasta"
]

freq={}

# Time complexity -- O(n)
for order in orders:
    if order in freq:
        freq[order]+=1
    else:
        freq[order]=1

print(freq.items())

# If we have used list it would take O(n^2) to check frequency of every order