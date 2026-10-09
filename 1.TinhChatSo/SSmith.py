from math import *
def prime(n):
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            return False
    return n>1

def tcs(n):
    sum=0
    while n!=0:
        sum+=n%10
        n//=10
    return sum

def tong(n):
    sum=0
    for i in range(2, isqrt(n)+1, 1):
        while n%i==0:
            sum+=tcs(i)
            n//=i
    if n!=1:
        sum+=tcs(n)
    return sum
    
if __name__=='__main__':
    n=int(input())
    if prime(n)==False and tcs(n)==tong(n):
        print('YES')
    else:
        print('NO')