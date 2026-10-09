#http://oj.28tech.com.vn/problem/oop24
class sv:
    def __init__(self, stt, ht, lop, ntns, gpa):
        self.stt=stt
        self.ht=ht
        self.ht=self.ht.title()
        self.lop=lop
        self.ntns=ntns
        if self.ntns[1]=='/':
            self.ntns='0'+self.ntns
        if self.ntns[4]=='/':
            self.ntns=self.ntns[0:3:]+'0'+self.ntns[3::]
        self.gpa=gpa
    def __str__(self):
        return f"SV{'{:03d}'.format(self.stt)} {self.ht} {self.lop} {self.ntns} {'{:.2f}'.format(self.gpa)}"
    
if __name__=="__main__":
    m=int(input())
    a=[]
    for i in range(1, m+1):
        ht=input()
        lop=input()
        ntns=input()
        gpa=float(input())
        a.append(sv(i, ht, lop, ntns, gpa))
    a.sort(key=lambda x: -x.gpa)
    for item in a:
        print(item)
