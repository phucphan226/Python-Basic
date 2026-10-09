from math import *
prime=[1]*100000000
def sang(n):
    prime[0], prime[1]=0, 0
    for i in range(2, isqrt(n)+1, 1):
        if prime[i]==1:
            for j in range(i*i, n+1, i):
                prime[j]=0
    for i in range(0, n+1):
        if prime[i]==1:
            print(i, end=' ')

if __name__=='__main__':
    n=int(input())
    sang(n)