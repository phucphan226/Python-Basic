n=int(input())
l, r=map(int, input().split())
a=list(map(int, input().split()))
cnt=[0]*n
cnt[0]=a[0]
for i in range(1, n, 1):
    cnt[i]=cnt[i-1]+a[i]
if l==0:
    print(cnt[r])
else:
    print(cnt[r]-cnt[l-1])