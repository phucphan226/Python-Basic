from functools import *

def tong(n):
    tong=0
    while n!=0:
        tong+=n%10
        n//=10
    return tong

def cmp(a, b):
    if tong(a)==tong(b):
        return a-b
    else:
        return tong(a)-tong(b)

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    #functools
    a.sort(key=cmp_to_key(cmp))
    #Lambda
    a.sort(key= lambda x: (sum(x), x))
    print(a)