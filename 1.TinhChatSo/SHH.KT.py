#Có tổng các ước không kể chính nó bằng chính nó.
from math import *
def perfect1(n):
    tong=1
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            tong+=i+n//i
            if i*i==n:
                tong-=i
    return tong==n

#Nếu p và 2^p-1 là số nguyên tố thì (2^p-1)*(2^(p-1)) là số hoàn hảo
def prime(n):
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            return False
    return n>1

def perfect2(n):
    for i in range(2, 50, 1):
        if prime(i)==True and prime(2**i-1)==True:
            if (2**i-1)*(2**(i-1))==n:
                return True
    return False        
    
if __name__=='__main__':
    n=int(input())
    if perfect2(n)==True:
        print('YES')
    else:
        print('N0')