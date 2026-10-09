def check(a, l, r):
    if l>=r:
        return True
    else:
        if a[l]!=a[r]:
            return False
        else:
            return check(a, l+1, r-1)

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    if check(a, 0, n-1)==True:
        print('YES')
    else:
        print('NO')   