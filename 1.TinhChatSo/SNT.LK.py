#LK SNT trong đoạn từ 1 đến n
from math import *
def prime(n):
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            return False
    return n>1

if __name__=='__main__':
    n=int(input())
    for i in range(1, n+1, 1):
        if(prime(i)==True):
            print(i, end=' ')
