from collections import *
s=input()
#Mang danh dau:
cnt=[0]*256
for item in s:
    if cnt[ord(item)]!=0:
        cnt[ord(item)]+=1
    else:
        cnt[ord(item)]=1
for i in range(0, 256):
    if cnt[i]!=0:
        print(chr(i), cnt[i])
#Dict:
a=dict()
for item in s:
    if item in a:
        a[item]+=1
    else:
        a[item]=1
for (key, value) in sorted(a.items()):
    print(key, value)
#Counter:
b=dict(Counter(s))
b=list(b.items())
b.sort()
b=dict(b)
for (key, value) in b.items():
    print(key, value)

