#Phân tích duy nhất 3 thừa số nguyên tố khác nhau 
from math import *
def check(n):
    dem=0
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            dem+=1
            mu=0
            while n%i==0:
                mu+=1
                n//=i
            if mu!=1:
                return False
    if n!=1:
        dem+=1
    if dem==3:
        return True
    else:
        return False
    
if __name__=='__main__':
    n=int(input())
    if check(n)==True:
        print(1)
    else:
        print(0)