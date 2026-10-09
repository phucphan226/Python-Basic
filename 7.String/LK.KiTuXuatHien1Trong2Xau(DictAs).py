s1=input()
s2=input()
a, b=set(s1), set(s2)
d=set()
for item in a:
    d.add(item)
for item in b:
    d.add(item)
d=list(d)
d.sort(key=lambda x: ord(x))
for item in d:
    print(item, end='')