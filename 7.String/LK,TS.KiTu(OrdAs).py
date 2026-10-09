from collections import *
s=input()
#Mang danh dau:
cnt=[0]*256
for item in s:
    if cnt[ord(item)]!=0:
        cnt[ord(item)]+=1
    else:
        cnt[ord(item)]=1
for i in range(0, len(s)):
    if cnt[ord(s[i])]!=0:
        print(s[i], cnt[ord(s[i])])
        cnt[ord(s[i])]=0
#Dict:
a=dict()
for item in s:
    if item in a:
        a[item]+=1
    else:
        a[item]=1
for (key, value) in a.items():
    print(key, value)
#Counter:
b=dict(Counter(s))
for (key, value) in b.items():
    print(key, value)

