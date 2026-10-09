from math import *
def tong(n):
    tong=0
    for i in range(1, isqrt(n)+1, 1):
        if n%i==0:
            tong+=i+n//i
            if i*i==n:
                tong-=i
    return tong

if __name__=='__main__':
    n=int(input())
    print(tong(n))