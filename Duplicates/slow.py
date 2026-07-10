# Slow Method
def duplicate_slow(list1):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i!=j and list1[i]==list1[j]:
                return True
            
    return False

numbers = [1,2,3,4,5,6,7,8,2]

result=duplicate_slow(numbers)

if result:
    print("Duplicate Found.")
else:
    print("No Duplicate Found.")