n=int(input())
a=list(map(int, input().split()))
#set:
b=set()
for x in a:
    if x not in b:
        print(x, end=' ')
        b.add(x)
#dict:
c={x: 1 for x in a}
for key in c:
    print(key, end=' ')