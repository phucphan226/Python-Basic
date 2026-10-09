delta=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
def floodFill(i, j):
    global check
    for item in delta:
        p, h=i+item[0], j+item[1]
        if p>=0 and p<n and h>=0 and h<m:
            if a[p][h]>=a[i][j]:
                check=0
                break
if __name__=='__main__':
    n, m=map(int, input().split())
    a=[]
    count=0
    for i in range(0, n):
        a.append(list(map(int, input().split())))
    for i in range(0, n):
        for j in range(0, m):
            check=1
            floodFill(i, j)
            if check==1:
                count+=1
    print(count)