n, m=map(int, input().split())
a=[0]*n
for i in range(0, n):
    a[i]=list(map(int, input().split()))
p, q=map(int, input().split())
b=[0]*p
for i in range(0, p):
    b[i]=list(map(int, input().split()))
c=[0]*n
for i in range(0, n):
    for j in range(0, q):
        for k in range(0, m):
            c[i][j]+=a[i][k]*b[k][j]
print(c)