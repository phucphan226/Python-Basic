class person:
    def __init__(self, ht, ntns, qq):
        self.ht=ht
        self.ht=self.ht.title()
        self.ntns=ntns
        if self.ntns[1]=='/':
            self.ntns='0'+self.ntns
        if self.ntns[4]=='/':
            self.ntns=self.ntns[0:3:]+'0'+self.ntns[3::]
        self.qq=qq
    def __str__(self):
        return self.ht+' '+self.ntns+' '+self.qq
class sinhVien(person):
    def __init__(self, msv, ht, ntns, qq, lop, gpa):
        person.__init__(self, ht, ntns, qq)
        self.msv=msv
        self.lop=lop
        self.gpa=gpa
    def __str__(self):
        return self.msv+' '+person.__str__(self)+' '+self.lop+' '+'{:.2f}'.format(self.gpa)
class giaoVien(person):
    def __init__(self, mgv, ht, ntns, qq, khoa, luong):
        person.__init__(self, ht, ntns, qq)
        self.mgv=mgv
        self.khoa=khoa
        self.luong=luong
    def __str__(self):
        return self.mgv+' '+person.__str__(self)+' '+self.khoa+' '+str(self.luong)
if __name__=="__main__":
    n=int(input())
    a=[]
    b=[]
    for i in range(1, n+1):
        s=input()
        if s[0:2]=="SV":
            ht=input()
            ntns=input()
            qq=input()
            lop=input()
            gpa=float(input())
            a.append(sinhVien(s, ht, ntns, qq, lop, gpa))
        elif s[0:2]=="GV":
            ht=input()
            ntns=input()
            qq=input()
            khoa=input()
            luong=int(input())
            b.append(giaoVien(s, ht, ntns, qq, khoa, luong))
    a.sort(key=lambda x: (-x.gpa, x.msv))
    b.sort(key=lambda x: (-x.luong, x.mgv))
    print("DANH SACH GIAO VIEN : ")
    for item in b:
        print(item)
    print("DANH SACH SINH VIEN : ")
    for item in a:
        print(item)        
