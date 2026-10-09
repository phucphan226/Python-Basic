s=input()
t=s.split()
b=set()
for item in t:
    if item not in b:
        print(item, end=' ')
        b.add(item)