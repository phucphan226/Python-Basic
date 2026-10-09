def first(a, k, l, r):
    res=-1
    while l<=r:
        m=(l+r)//2
        if a[m]==k:
            res=m
            r=m-1
        elif a[m]<k:
            l=m+1
        else:
            r=m-1
    return res

def last(a, k, l, r):
    res=-1
    while l<=r:
        m=(l+r)//2
        if a[m]==k:
            res=m
            l=m+1
        elif a[m]<k:
            l=m+1
        else:
            r=m-1
    return res

def first1(a, k, l, r):
    res=-1
    while l<=r:
        m=(l+r)//2
        if a[m]>k:
            res=m
            r=m-1
        else:
            l=m+1
    return res

def last1(a, k, l, r):
    res=-1
    while l<=r:
        m=(l+r)//2
        if a[m]<k:
            res=m
            l=m+1
        else:
            r=m-1
    return res

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    k=int(input())
    for i in range(0, n, 1):
        print(i, end=' ')
    print()
    for i in a:
        print(i, end=' ')
    print()
    print(first(a, k, 0, n-1), last(a, k, 0, n-1), first1(a, k, 0, n-1), last1(a, k, 0, n-1))