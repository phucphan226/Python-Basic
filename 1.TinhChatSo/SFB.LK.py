from math import *
def lk(n):
    if n==1:
        print('0')
    elif n==2:
        print('0 1')
    else:
        print('0 1', end=' ')
        f1, f2=0, 1
        for i in range(3, n+1, 1):
            fn=f1+f2
            print(fn, end=' ')
            f1, f2=f2, fn
            
if __name__=='__main__':
    n=int(input())
    lk(n)