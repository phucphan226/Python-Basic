#Một số nguyên dương chẵn >=4 đều có thể biểu diễn dưới dạng tổng của 2 số nguyên tố
from math import *
def prime(n):
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            return False
    return n>1
if __name__=='__main__':
    n=int(input())
    for i in range(1, n+1, 1):
        m=int(input())
        for j in range(2, m//2+1, 1):
            if prime(j)==True and prime(m-j)==True:
                print(j, m-j)
