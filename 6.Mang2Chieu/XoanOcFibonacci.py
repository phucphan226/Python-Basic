f=[0]*100
def fibo():
    f[1], f[2]=0, 1
    for i in range(3, 100):
        f[i]=f[i-1]+f[i-2]

if __name__=='__main__':
    fibo()
    u=int(input())
    count, m, n, p, q=1, 0, u-1, 0, u-1
    a=[[0 for x in range(0, u)] for x in range(0, u)]
    while count<=u*u:
        for i in range(m, n+1):
            a[p][i]=f[count]
            count+=1
        p+=1
        for i in range(p, q+1):
            a[i][n]=f[count]
            count+=1
        n-=1
        for i in range(n, m-1, -1):
            a[q][i]=f[count]
            count+=1
        q-=1
        for i in range(q, p-1, -1):
            a[i][m]=f[count]
            count+=1
        m+=1
    for i in range(0, u):
        for j in range(0, u):
            print(a[i][j], end=' ')
        print()