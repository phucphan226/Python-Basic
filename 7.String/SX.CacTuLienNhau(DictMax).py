from functools import *
def cat(a, b):
    x, y=a+b, b+a
    if x<y:
        return 1
    else:
        return -1
if __name__=='__main__':
    n=int(input())
    s=input()
    s=s.split()
    s.sort(key=cmp_to_key(cat))
    print(''.join(s))
