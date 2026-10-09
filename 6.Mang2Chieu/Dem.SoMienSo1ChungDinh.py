delta=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def floodFill(i, j):
    a[i][j]=0
    for item in delta:
        p, h=i+item[0], j+item[1]
        if p>=0 and p<n and h>=0 and h<m and a[p][h]==1:
            floodFill(p, h)

if __name__=='__main__':
    n, m=map(int, input().split())
    a=[[0 for x in range(0, m)] for x in range(0, n)]
    count=0
    for i in range(0, n):
        a[i]=list(map(int, input().split()))
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j]==1:
                count+=1         
                floodFill(i, j)
    print(count)