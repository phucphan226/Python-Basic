delta=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
n, m=map(int, input().split())
a=[0]*n
for i in range(0, n):
    a[i]=list(map(int, input().split()))
p, h=map(int, input().split())
for item in delta:
    if p+item[0]>=0 and p+item[1]<n and h+item[0]>=0 and h+item[1]<m:
        print(a[p+item[0]][h+item[1]], end=' ')