# Power of a number using recursion

def power(number,exponent):
    if exponent==0:
        return 1
    else:
        return number * power(number,exponent-1)
    
print(power(2,3))