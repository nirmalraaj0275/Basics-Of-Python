n = int(input())
org = n
k = len(str(n))
sum1 = 0

for i in range(k):
    id = n% 10 
    sum1 += id ** k
    n = n//10
if sum1 == org:
    print("YES")
else:
    print("NO")