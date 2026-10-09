m, n=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(set(a).symmetric_difference(set(b)))
c.sort()
for item in c:
    print(item, end=' ')