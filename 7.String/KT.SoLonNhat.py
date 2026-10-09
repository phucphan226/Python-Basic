s=input()
t=''
for item in s:
    if item.isalpha()==True:
        t+=' '
    else:
        t+=item
t=list(map(int, t.split()))
print(max(t))