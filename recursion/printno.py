# Print numbers from 1 to n using recursion
def display(n):
    if n==1:
        print("1", end=" ")
        return
    else:
        display(n-1)
    print(n, end=" ")

display(8)