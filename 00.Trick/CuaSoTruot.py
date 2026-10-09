n, k=map(int, input().split())
a=list(map(int, input().split()))
tong=sum(a[0:k:1])
print(tong, end=' ')
for i in range(1, n-k+1, 1):
    tong=tong-a[i-1]+a[i+k-1]
    print(tong, end=' ')

