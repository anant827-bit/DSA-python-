# Print numbers in reverse order using recursion upto 1
def rev_display(n):
    if n==1:
        print('1', end=" ")
        return
    else:
        print(n, end=" ")
        rev_display(n-1)

rev_display(8)