n = list(map(int,input().split()))
large = n[0]
for i in range(len(n)-1):
    if large < n[i]:
        large = n[i]
print(large)