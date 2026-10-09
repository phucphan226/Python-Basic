n=int(input())
a=list(map(int, input().split()))
a.sort()
ans, cnt, res=1, 1, a[0]
for i in range(1, n, 1):
    if a[i]==a[i-1]:
        cnt+=1
    else:
        if cnt>ans:
            ans=cnt
            res=a[i-1]
        cnt=1
    if i==n-1 and cnt>ans:
        ans=cnt
        res=a[i-1]
print(res, ans)