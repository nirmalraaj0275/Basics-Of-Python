def printArray(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()

def reversed1(arr,n):
    ans = [0]*n
    for i in range (n-1,-1,-1):
        ans[n-1-i]=arr[i]
    printArray(ans,n)
    
arr=[1,2,3,4,5]
n = len(arr)
reversed1(arr,n)