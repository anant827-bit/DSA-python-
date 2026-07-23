# Reverse a string using recursion

def rev_str(string,length):
    if length==0:
        return ""
    else:
        return string[length-1] + rev_str(string, length-1)
    

print(rev_str("Python", 6))