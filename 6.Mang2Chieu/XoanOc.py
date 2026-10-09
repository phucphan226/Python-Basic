u=int(input())
a=[[0 for x in range(0, u)] for x in range(0, u)]
count, m, n, p, q=1, 0, u-1, 0, u-1
while count<=u*u:
    for i in range(m, n+1):
        a[p][i]=count
        count+=1
    p+=1
    for i in range(p, q+1):
        a[i][n]=count
        count+=1
    n-=1
    for i in range(n, m-1, -1):
        a[q][i]=count
        count+=1
    q-=1
    for i in range(q, p-1, -1):
        a[i][m]=count
        count+=1
    m+=1
for i in range(0, u):
    for j in range(0, u):
        print(a[i][j], end=' ')
    print()
