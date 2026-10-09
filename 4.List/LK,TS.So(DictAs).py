n=int(input())
a=list(map(int, input().split()))
a.sort()
cnt, ans, res=1, 1, a[0]
for i in range(1, n, 1):
    if a[i]==a[i-1]:
        cnt+=1
    else:
        print(a[i-1], cnt)
        cnt=1
    if i==n-1:
        print(a[i], cnt)