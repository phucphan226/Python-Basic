def last(a, x, l, r):
    pos=-1
    while l<=r:
        m=(l+r)//2
        if a[m]<x:
            pos=m
            l=m+1
        else:
            r=m-1
    return pos

if __name__=='__main__':
    n, k=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()
    cnt=0
    for i in range(0, len(a)-1, 1):
        if last(a, k-a[i], i+1, n-1)!=-1:
            cnt+=last(a, k-a[i], i+1, n-1)-i
    print(cnt)