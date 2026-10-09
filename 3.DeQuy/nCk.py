def nCk(n, k):
    if n==k or k==0:
        return 1
    else:
        return nCk(n-1, k-1)+nCk(n-1, k)

if __name__=='__main__':
    n, k=map(int, input().split())
    print(nCk(n, k))