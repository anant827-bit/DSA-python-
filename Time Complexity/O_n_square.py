# Time Complexity -- O(n^2)
def find_duplicates(numbers): 
    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)):
            if (i!=j and numbers[i]==numbers[j]):
                return True
            
    return False
            
numbers=[1,2,3,4,5,3]

result=find_duplicates(numbers)

if(result):
    print("Duplicates found.")
else:
    print("No duplicates found.")