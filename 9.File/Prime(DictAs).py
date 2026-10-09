from math import *
def prime(n):
    for i in range(2, isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
if __name__=="__main__":
    f1=open("Prime.input.txt", "r")
    f2=open("Prime.output.txt", "w")
    s=f1.readline()
    a=list(map(int, s.split()))
    a.sort()
    b=set()
    for item in a:
        if prime(item) and item not in b:
            b.add(item)
            f2.write(str(item)+' ')
    f1.close()
    f2.close()