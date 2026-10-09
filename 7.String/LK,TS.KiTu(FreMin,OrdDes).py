s=input()
a=dict()
for item in s:
    if item in a:
        a[item]+=1
    else:
        a[item]=1
c=list(a.items())
c.sort(key=lambda x: (x[1], -ord(x[0])))
print(c[0][0], c[0][1])