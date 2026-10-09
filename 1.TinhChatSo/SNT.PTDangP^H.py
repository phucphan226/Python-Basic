from math import *
def uoc(n):
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            dem=0
            while(n%i==0):
                dem+=1
                n//=i
            print(i, '^', dem, sep='', end='')
            if n!=1:
                print(' * ', end='')
    if n!=1:
        print(n, 1, sep='^')


if __name__=='__main__':
    n=int(input())
    uoc(n)

