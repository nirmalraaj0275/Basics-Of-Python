n = list(map(int,input().split()))


# for i in n:
#     if i not in a:
#         a.append(i)
#     else:
#         i+= 1
# print(a)

# TWO POINTER
i = 0
for j in range(1,len(n)):
    if n[i] != n[j]:
        i+=1
        n[i]=n[j]
k = i+1
for i in range(k):
    print(n[i],end=" ")