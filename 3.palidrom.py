n = list(map(int,input().strip()))
a =[]
for i in range(len(n)-1,-1,-1):
    a.append(n[i])
if a == n:
    print("Palidrom")
else:
    print("Not Palidrom")