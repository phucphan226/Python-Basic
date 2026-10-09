s=input()
s=s.split()
a=dict()
for item in s:
    if item in a:
        a[item]+=1
    else:
        a[item]=1
b=list(a.items())
b.sort(key=lambda x: (x[1], x[0]), reverse=True)
print(b[0][0], b[0][1])