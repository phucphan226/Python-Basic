s=input()
#C1:
a=set()
b=""
for i in range(0, len(s)):
    if i==0:
        b=s[0]
    elif i==len(s)-1:
        if s[i]==s[i-1]:
            b+=s[i]
            a.add(b)
        else:
            a.add(b)
            b=s[i]
            a.add(b)
    else:
        if s[i]==s[i-1]:
            b+=s[i]
        else:
            a.add(b)
            b=s[i]
a=list(a)
a.sort(key=lambda x: (len(x), x), reverse=True)
print(a[0])
#C2:
cnt, tmp, res, mcnt=1, s[0], s[0], 1
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        tmp+=s[i]
        cnt+=1
    else:
        if cnt==mcnt:
            if tmp>res:
                res=tmp    

        elif cnt>mcnt:
            res=tmp
            mcnt=cnt
        tmp=s[i]
        cnt=1
    if i==len(s)-1:
        if cnt==mcnt:
            if tmp>res:
                res=tmp
    if cnt>mcnt:
        res=tmp
        mcnt=cnt
print(res)
