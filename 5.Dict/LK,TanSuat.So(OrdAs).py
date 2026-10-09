n=int(input())
a=list(map(int, input().split()))
b=dict()
for x in a:
    if x in b:
        b[x]+=1
    else:
        b[x]=1
for x, y in b.items():
    print(x, y)
