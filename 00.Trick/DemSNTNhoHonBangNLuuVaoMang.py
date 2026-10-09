from math import*
prime=[1]*(10**6+1)
def sang():
    prime[0], prime[1]=0, 0
    for i in range(2, isqrt(10**6+1)+1,  1):
        if prime[i]==1:
            for j in range(i*i, 10**6+1, i):
                prime[j]=0

p=[0]*(10**6+1)
def P():
    p[0], p[1]=0, 0
    for i in range(2, 10**6+1, 1):
        p[i]=p[i-1]+prime[i]

if __name__=='__main__':
    sang()
    P()
    n=int(input())
    print(p[n])