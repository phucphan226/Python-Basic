s=input()
s=s.split()
print(' '.join(s).title())
t=input()
if t[1]=='/':
    t='0'+t
if t[4]=='/':
    t=t[0:3:]+'0'+t[3::]
print(t)

