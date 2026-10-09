n=int(input())
a=[[0 for _ in range(0, n)] for _ in range(0, n)]
for i in range(0, n):
    a[i]=list(map(int, input().split()))
for i in range(0, n):
    a[i][i], a[i][n-1-i]=a[i][n-1-i], a[i][i]
for i in range(0, n):
    for j in range(0, n):
        print(a[i][j], end=' ')
    print()