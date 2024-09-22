def numbers(n):
    if n <=0:
        return 
    print(n,end=" ") 
    return numbers(n-1)
numbers(5)