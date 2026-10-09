m, n=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
b=list(set(a).union(set(b)))
b.sort(reverse=True)
for item in b:
    print(item, end=' ')
