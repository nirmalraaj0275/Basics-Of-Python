n1 = int(input())
n2 = int(input())

##METHOD 1
gcd = 1
for i in range(1,min(n1,n2)+1,1):
    if n1%i == 0 and n2%i == 0 :
        gcd = i
print(gcd)


#METHOD 2
gcd = 1
for i in range(max(n1, n2), 0, -1):  
    if n1 % i == 0 and n2 % i == 0:  
        gcd = i
        break
print(gcd)



