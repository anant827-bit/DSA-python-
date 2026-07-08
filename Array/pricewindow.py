prices=[2,4,6,1,7,3,5]

def max(prices, windowsize):
    current_total=sum(prices[0:windowsize])
    best_total=current_total

    print(f"Window 1: {prices[0:windowsize]} = {current_total}")

    for i in range(windowsize, len(prices)):
        left=prices[i-windowsize]
        right=prices[i]

        current_total=current_total-left+right

        window=prices[i-windowsize+1:i+1]
        print(f"Window: {window} = {current_total}")

        if current_total>best_total:
            best_total=current_total

    return best_total

result=max(prices, 3)
print(result)