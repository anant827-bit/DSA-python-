# Fibonacci Series -- 0 1 1 2 3 5 8...
def fibonacci(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)
    
print("Fibonacci Series:", end="")
for i in range(0,7):
    print(fibonacci(i), end=", ")