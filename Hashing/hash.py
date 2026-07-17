# Hashing in Python is done using dictionaries & sets

# Using list
users = [
    "anant@gmail.com",
    "vaibhavi@gmail.com",
    "ishu@gmail.com"
]

find="vaibhavi@gmail.com"

#Time Complexity -- O(n)
def find_user(users, find):
    for user in users:   
        if find == user:
            return "User Found."
    return "Not Found."

print(find_user(users, find))

# Using dictionary
username_dict = {"anant@gmail.com":"anant8", "vaibhavi@gmail.com":"vaibhavi27", "ishu@gmail.com":"ishu827"}

#Time Complexity -- O(1)
if find in username_dict:  
    print("Found.")
else:
    print("Not Found.")


# Using Set
user_online=set()
user_online.add("vaibhavi@gmail.com")
user_online.add("anant@gmail.com")
user_online.add("ishu@gmail.com")

print(user_online)

# Time Complexity -- O(1)
print("ishu@gmail.com" in user_online)