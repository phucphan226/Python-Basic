n, m=map(int, input().split())
a=[0]*n
for i in range(0, n):
    a[i]=list(map(int, input().split()))
b=[x for small_list in a for x in small_list]
print(b)