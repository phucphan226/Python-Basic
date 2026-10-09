f1=open("ChuanHoaTen-Phay.input.txt", "r")
f2=open("ChuanHoaTen-Phay.output.txt", "w")
s=f1.readline()
a=[]
b=""
for i in range(0, len(s)):
    if s[i]!=',':
        b+=s[i]
    else:
        a.append(b)
        b=""
a.append(b)
for i in range(0, len(a)):
    a[i]=(' '.join(a[i].split())).title()
    f2.write(a[i])
    if i!=len(a)-1:
        f2.write(',')
f1.close()
f2.close()