from math import *
def lk(n):
    for i in range(1, isqrt(n)+1, 1):
        if n%i==0:
            print(i, end=' ')
    for i in range(isqrt(n)+1, 0, -1):
        if n%i==0 and i*i!=n:
            print(n//i, end=' ')
if __name__=='__main__':
    n=int(input())
    lk(n)