def mail(line):
    line=line.lower()
    a=line.split()
    line=a[2]+a[0][0]+a[1][0]
    if line in b:
        b[line]+=1
    else:
        b[line]=1
    line+=str(b[line])+"@gmail.com"
    return line

def passWord(line):
    b=line.split('/')
    line=str(int(b[0]))+str(int(b[1]))+str(int(b[2]))
    return line
if __name__=="__main__":
    f1=open("CapMail.input.txt", "r")
    f2=open("CapMail.output.txt", "w")
    b=dict()
    n=0
    for line in f1:
        n+=1
        if n%2!=0:
            f2.write(mail(line)+'\n')
        else:
            f2.write(passWord(line)+'\n')
    f1.close()
    f2.close()