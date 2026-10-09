from collections import *
n=int(input())
a=list(map(int, input().split()))
#set:
print(len(set(a)))
#dict:
b={x: 1 for x in a}
print(len(b))
#Counter:
c=Counter(a)
c=list(c)
print(len(c))
