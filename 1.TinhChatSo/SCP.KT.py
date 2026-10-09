from math import *
def square(n):
    can=isqrt(n)
    return can*can==n

if __name__=='__main__':
    n=int(input())
    if square(n)==True:
        print('YES')
    else:
        print('NO')