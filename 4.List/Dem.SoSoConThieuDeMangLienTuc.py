n=int(input())
a=list(map(int, input().split()))
a.sort()
cnt=0
for i in range(1, len(a), 1):
    if a[i]-a[i-1]>1:
        cnt+=a[i]-a[i-1]-1
print(cnt)