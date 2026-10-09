n, m=map(int, input().split())
a=[0]*n
maxg=-1e9
for i in range(0, n):
    a[i]=list(map(int, input().split()))
f=[[0 for _ in range(0, m)] for _ in range(0, n)]
for i in range(0, n):
    for j in range(0, m):
        if i==0 and j==0:
            f[i][j]=a[i][j]
        elif i==0:
            f[i][j]=f[i][j-1]+a[i][j]
        elif j==0:
            f[i][j]=f[i-1][j]+a[i][j]
        else:
            f[i][j]=max(f[i-1][j]+a[i][j], f[i][j-1]+a[i][j])
print(f[n-1][m-1])
