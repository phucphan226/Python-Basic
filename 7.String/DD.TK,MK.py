n=int(input())
a=dict()
for i in range(0, n):
    s=input()
    s=s.lower()
    s=s.split()
    tk=''
    tk+=s[len(s)-2]
    for i in range(0, len(s)-2):
        tk+=s[i][0]
    if tk in a:
        a[tk]+=1
        print(tk, a[tk], "@gmail.com", sep='')
    else:
        a[tk]=1
        print(tk, a[tk], "@gmail.com", sep='')
    mk=s[len(s)-1]
    mk=mk.split('/')
    for item in mk:
        print(int(item), end='')
    print()