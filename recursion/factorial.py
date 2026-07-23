# Factorial of a number -- n!
def factorial(number):
    if number<0:
        return "Error: Enter a positive number."
    elif number==0 or number==1:
        return 1
    else:
        return number * factorial(number-1)
    
print("Factorial of 5:", factorial(5))