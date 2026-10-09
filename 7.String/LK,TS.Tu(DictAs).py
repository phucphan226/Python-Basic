s=input()
s=s.split()
a=dict()
for item in s:
    if item in a:
        a[item]+=1
    else:
        a[item]=1
for (key, value) in sorted(a.items()):
    print(key, value)