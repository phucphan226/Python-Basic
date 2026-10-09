delta=[[-1, 0], [0, -1], [0, 1], [1, 0]]
def floodFill(i, j):
    global count
    count+=1
    a[i][j]=0
    for item in delta:
        p, h=i+item[0], j+item[1]
        if p>=0 and p<n and h>=0 and h<m and a[p][h]==1:
            floodFill(p, h)

if __name__=="__main__":
    n, m=map(int, input().split())
    a=[[0 for _ in range(0, n)] for _ in range(0, n)]
    for i in range(0, n):
        a[i]=list(map(int, input().split()))
    maxc=-1e9
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j]==1:
                count=0
                floodFill(i, j)
                if count>maxc:
                    maxc=count
    print(maxc)
