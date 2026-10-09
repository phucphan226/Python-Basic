s=input()
a=dict()
for item in s:
    if item in a:
        a[item]+=1
    else:
        a[item]=1
sum=len(s)
for (key, value) in a.items():
    if value>=2:
        sum+=value*(value-1)//2
print(sum)