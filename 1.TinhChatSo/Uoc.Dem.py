from math import *
def dem(n):
    dem=0
    for i in range(1, isqrt(n)+1, 1):
        if n%i==0:
            dem+=2
            if i*i==n:
                dem-=1
    return dem

if __name__=='__main__':
    n=int(input())
    print(dem(n))