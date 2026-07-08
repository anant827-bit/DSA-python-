# Find the highest sum of three consequetive indices --  2 4 6 1 7 3 5

def sum_three(numbers):
    max=0
    length=len(numbers)

    for i in range(length-2):
        if max < numbers[i]+numbers[i+1]+numbers[i+2]:
            max=numbers[i]+numbers[i+1]+numbers[i+2]
            index=i

    return max, index

numbers=[2,4,6,1,7,3,5]
a,b=sum_three(numbers)
print(f"{a} and {b}")

# Method 2
def sliding(numbers):
    left=0
    length=len(numbers)
    max=0
    for right in range(2,length):
        if max < sum(numbers[left:right+1]):
            max=sum(numbers[left:right+1])
        left = left+1
    return max, left-1

m, index=sliding(numbers)
print(f"{m},{index}")       