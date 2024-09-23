n = list(map(int,input().split()))

large = 0
seclarge = 0

for i in range (len(n)-1):
    if n[i] > large:
        seclarge = large
        large = n[i]
        
print("secound largest Number is:",seclarge)