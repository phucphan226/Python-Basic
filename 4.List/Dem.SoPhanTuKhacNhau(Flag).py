cnt=[0]*10000000
n=int(input())
a=list(map(int, input().split()))
for i in a:
    cnt[i]=1
dem=0
for i in a:
    if cnt[i]!=0:
        dem+=1
        cnt[i]=0
print(dem)