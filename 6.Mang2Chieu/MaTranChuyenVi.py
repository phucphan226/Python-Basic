n, m=map(int, input().split())
a=[0]*n
for i in range(0, n):
    a[i]=list(map(int, input().split()))
b=[[x[i] for x in a] for i in range(0, m)]
print(b)