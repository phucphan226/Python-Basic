from functools import *
def cmp(a, b):
    x, y=a+b, b+a
    if x>y:
        return -1
    else:
        return 1
if __name__=="__main__":
    s=input()
    t=""
    for item in s:
        if item.isalpha()==True:
            t+=' '
        else:
            t+=item
    t=list(map(int, t.split()))
    t=list(map(str, t))
    t.sort(key=cmp_to_key(cmp))
    for item in t:
        print(item, end='')