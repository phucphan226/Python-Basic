n=int(input())
a=list(map(int, input().split()))
cnt=[0]*10000000
for i in a:
    cnt[i]+=1
for i in a:
    if cnt[i]!=0:
        print(i, cnt[i])
        cnt[i]=0