from math import*
def kt(n):
    f1, f2=0, 1
    if n==0 or n==1:
        return True
    for i in range(3, 100, 1):
        fn=f1+f2
        if fn==n:
            return True
        f1, f2=f2, fn
    return False

if __name__=='__main__':
    n=int(input())
    if kt(n)==True:
        print('YES')
    else:
        print('NO')