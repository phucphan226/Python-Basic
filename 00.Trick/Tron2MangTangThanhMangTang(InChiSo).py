def merge(b, c, m, n):
    i, j=0, 0
    while i<m and j<n:
        if b[i]<=c[j]:
            print('b', i+1, sep='', end=' ')
            i+=1
        else:
            print('c', j+1, sep='', end=' ')
            j+=1
    while i<m:
        print('b', i+1, sep='', end=' ')
        i+=1
    while j<n:
        print('c', j+1, sep='', end=' ')
        j+=1
    

if __name__=='__main__':
    m, n=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    a.sort()
    b.sort()
    merge(a, b, m, n)