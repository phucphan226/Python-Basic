#http://oj.28tech.com.vn/problem/oop32
class sv:
    def __init__(self, msv, ht, lop, mail):
        self.msv=msv
        self.ht=ht
        self.ht=(' '.join(self.ht.split())).title()
        self.lop=lop
        self.mail=mail
    def __str__(self):
        return f"{self.msv} {self.ht} {self.lop} {self.mail}"
    
if __name__=="__main__":
    n=int(input())
    a=[]
    for i in range(1, n+1):
        msv=input()
        ht=input()
        lop=input()
        mail=input()
        a.append(sv(msv, ht, lop, mail))
    m=int(input())
    for i in range(1, m+1):
        tmp=input()
        print("DANH SACH SINH VIEN KHOA", tmp, ":")
        for item in a:
            if item.msv[0:4]==tmp:
                print(item)
