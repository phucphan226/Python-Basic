a=list(map(str, input().split()))
b=dict()
for x in a:
    if x in b:
        b[x]+=1
    else:
        b[x]=1
b=list(b.items())
b.sort(key=lambda x: (-x[1], x[0]))
b=dict(b)
for x, y in b.items():
    print(x, y)