def find_two_numbers(numbers, sum):
    left=0
    right=len(numbers)-1

    while(left<=right):
        if(sum==numbers[left]+numbers[right]):
            return left,right
        elif(sum>numbers[left]+numbers[right]):
            left=left+1
        else:
            right=right-1
    return -1,-1
    
numbers=[1,2,3,4,5,6]
sum=8

a,b = find_two_numbers(numbers, sum)

if(a==b==-1):
    print("Not found")
else:
    print(f"Found at {a} and {b}")