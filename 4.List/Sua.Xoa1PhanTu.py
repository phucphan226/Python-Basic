n, k=map(int, input().split())
a=list(map(int, input().split()))
b=a[0:k:1]
b+=a[k+1:len(a):1]
for item in b:
    print(item, end=' ')