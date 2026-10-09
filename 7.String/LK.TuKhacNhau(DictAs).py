s=input()
t=s.split()
c=list(set(t))
c.sort()
for item in c:
    print(item, end=' ')