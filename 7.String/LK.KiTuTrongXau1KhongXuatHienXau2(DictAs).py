s1=input()
s2=input()
a, b=set(s1), set(s2)
c=set()
for item in a:
    if item not in b:
        c.add(item)
c=list(c)
c.sort(key=lambda x: x[0])
for item in c:
    print(item, end='')
