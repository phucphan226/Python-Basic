s=input()
cnt, tmp, res, mcnt=1, s[0], s[0], 1
for i in range(1, len(s)):
    if s[i]!=s[i-1]:
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
