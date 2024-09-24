arr = list(map(int,input().split()))
n = len(arr)
temp= [0]*n
for i in range(1,n):
    temp[i-1]=arr[i]
temp[n-1]=arr[0]
print(temp)

