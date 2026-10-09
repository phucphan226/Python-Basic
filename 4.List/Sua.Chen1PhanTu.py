n, x, k=map(int, input().split())
a=list(map(int, input().split()))
b=a[0:k:1]
tmp=[x]
b+=tmp
b+=a[k:len(a):1]
for item in b:
    print(item, end=' ')