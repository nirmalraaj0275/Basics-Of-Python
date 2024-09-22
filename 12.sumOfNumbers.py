def sums(n,sum1):
    if n < 0:
        return sum1
    sum1 += n
    return sums(n-1,sum1)
n = 5
sum1 = 0
print(sums(n,sum1))