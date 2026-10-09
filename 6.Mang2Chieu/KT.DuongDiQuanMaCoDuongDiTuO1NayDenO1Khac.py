delta=[[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
def floodFill(i, j):
    a[i][j]=0
    for item in delta:
        p, h=i+item[0], j+item[1]
        if p>=0 and p<n and h>=0 and h<n and a[p][h]==1:
            floodFill(p, h)


if __name__=="__main__":
    n=int(input())
    s, t, u, v=map(int, input().split())
    s, t, u, v=s-1, t-1, u-1, v-1
    a=[[0 for _ in range(0, n)] for _ in range(0, n)]
    for i in range(0, n):
        a[i]=list(map(int, input().split()))
    floodFill(s, t)
    if a[u][v]==0:
        print('YES')
    else:
        print('NO')
