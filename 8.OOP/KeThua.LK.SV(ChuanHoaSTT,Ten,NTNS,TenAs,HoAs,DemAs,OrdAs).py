class person:
    def __init__(self, ht, ntns, qq):
        self.ht=ht
        self.ht=self.ht.title()
        self.ho, self.dem, self.ten=self.ht.split()
        self.ntns=ntns
        if self.ntns[1]=='/':
            self.ntns='0'+self.ntns
        if self.ntns[4]=='/':
            self.ntns=self.ntns[0:3:]+'0'+self.ntns[3::]
        self.qq=qq
class sinhVien(person):
    def __init__(self, stt, ht, ntns, qq, lop, gpa):
        person.__init__(self, ht, ntns, qq)
        self.stt=stt
        self.lop=lop
        self.gpa=gpa
    def __str__(self):
        return f"{'{:04d}'.format(self.stt)} {self.ht} {self.ntns} {self.qq} {self.lop} {'{:.2f}'.format(self.gpa)}"

if __name__=="__main__":
    n=int(input())
    a=[]
    for i in range(1, n+1):
        ht=input()
        ntns=input()
        qq=input()
        lop=input()
        gpa=float(input())
        a.append(sinhVien(i, ht, ntns, qq, lop, gpa))
    a.sort(key=lambda x: (x.ten, x.ho, x.dem, x.stt))
    for item in a:
        print(item)