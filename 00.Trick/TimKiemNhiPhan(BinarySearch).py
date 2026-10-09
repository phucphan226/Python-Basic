def binarySearch(a, k, l, r):
    while l<=r:
        m=(l+r)//2
        if a[m]==k:
            return True
        elif a[m]>k:
            r=m-1
        else:
            l=m+1
    return False

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    k=int(input())
    if binarySearch(a, k, 0, n-1)==False:
        print('NO')
    else:
        print('YES')
