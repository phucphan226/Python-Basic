from math import *
def prime(n):
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            return False
    return n>1

if __name__=='__main__':
    n=int(input())
    if prime(n)==True:
        print('YES')
    else:
        print('NO')