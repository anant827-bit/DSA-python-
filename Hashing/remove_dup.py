# Removing duplicates from a set of list -- Checking exact number of online users removing multiple logins
email=[
    "anant@gmail.com",
    "vaibhavi@gmail.com",
    "anant@gmail.com",
    "vaibhavi@gmail.com",
    "ishu@gmail.com"
]

unique=[]
email_set=set()

for entry in email:
    if entry not in email_set:
        unique.append(entry)
    email_set.add(entry)

print("After removing duplicates:",unique)