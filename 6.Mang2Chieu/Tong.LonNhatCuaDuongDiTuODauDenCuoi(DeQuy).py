delta=[[0, 1], [1, 0]]
def go(i, j, tong):
    global maxg
    if i==n-1 and j==m-1:
        if tong>maxg:
            maxg=tong
    else:
        x, y, z, t=i+delta[0][0], j+delta[0][1], i+delta[1][0], j+delta[1][1]
        if x>=0 and x<n and y>=0 and y<m:
            go(x, y, tong+a[x][y])
        if z>=0 and z<n and t>=0 and t<m:
            go(z, t, tong+a[z][t])

if __name__=='__main__':
    n, m=map(int, input().split())
    a=[0]*n
    maxg=-1e9
    for i in range(0, n):
        a[i]=list(map(int, input().split()))
    go(0, 0, a[0][0])
    print(maxg)