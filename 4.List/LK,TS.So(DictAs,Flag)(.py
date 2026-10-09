n=int(input())
a=list(map(int, input().split()))
cnt=[0]*10000000
for i in a:
    cnt[i]+=1
for i in range(0, max(a)+1, 1):
    if cnt[i]!=0:
        print(i, cnt[i])