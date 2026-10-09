s=input()
t=input()
s, t=s.lower(), t.lower()
s, t=s.split(), t.split()
a, b=set(s), set(t)
c=list(a.intersection(b))
for item in sorted(c):
    print(item, end=' ')