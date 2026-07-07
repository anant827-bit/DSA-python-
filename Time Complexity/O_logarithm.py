# Time Complexity -- O(logn)
def find_name(names, target):
    left=0
    right=len(names)-1
    
    while(left<=right):
        middle=(left+right)//2

        if(names[middle]==target):
            return middle
        elif(names[middle]<target):
            left=middle+1
        else:
            right=middle-1

        return -1
    
names=["Anant", "Vaibhavi", "Ishu", "Raj", "Vishesh", "Aman"]
target="Ishu"

result=find_name(names, target)

if(result!=-1):
    print(f"Found at {result}")
else:
    print("Not Found")