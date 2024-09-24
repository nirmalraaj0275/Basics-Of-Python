arr = list(map(int,input().split()))
n = len(arr)
temp = [0]*(n)
for i in range(1,n):
    temp[i]=arr[i-1]
temp[0]=arr[n-1]
print(temp)