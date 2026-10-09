m, n=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
b=list(set(a).intersection(set(b)))
for item in a:
    if item in b:
        print(item, end=' ')
        b.remove(item)
