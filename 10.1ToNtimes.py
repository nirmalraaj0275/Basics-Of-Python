def numbers(i,n):
    if i>n:
        return 
    print(i,end=" ")
    return numbers(i+1,n)
numbers(1,5)