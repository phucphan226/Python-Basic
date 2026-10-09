class in4:
    def __init__(self, ht, mail, sdt, diem):
        self.ht=ht
        self.mail=mail
        self.sdt=sdt
        self.diem=diem
if __name__=="__main__":
    f1=open("TrungTuyen.input.txt", "r")
    f2=open("TrungTuyen.output.txt", "w")
    a=[]
    n=0
    for line in f1:
        n+=1
        if n%4==1:
            ht=line
        elif n%4==2:
            mail=line
        elif n%4==3:
            sdt=line
        else:
            t, l, h=map(float, line.split())
            diem=t+l+h
            if diem>=27:
                a.append(in4(ht, mail, sdt, diem))
    a.sort(key=lambda x: -x.diem)
    for item in a:
        f2.write(item.ht)
        f2.write(item.mail)
        f2.write(item.sdt)
        f2.write(str(item.diem)+'\n')
    f1.close()
    f2.close()