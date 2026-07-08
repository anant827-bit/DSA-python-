# remove duplicates from soted array
def delete_duplicates(names):
    names.sort()
    left=0
    for right in range(1,len(names)):
        if names[right]!=names[left]:
            left=left+1
            names[left]=names[right]
    return left+1

names=["Anant", "Vaibhavi", "Anant", "Divya", "Raj"]

count=delete_duplicates(names)

print(names[:count])