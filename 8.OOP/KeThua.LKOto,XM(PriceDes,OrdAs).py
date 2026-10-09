class car:
    def __init__(self, mx, tx, h, ms, gb):
        self.mx=mx
        self.tx=tx
        self.h=h
        self.ms=ms
        self.gb=gb
class xm(car):
    def __init__(self, mx, tx, h, ms, td, gb):
        car.__init__(self, mx, tx, h, ms, gb)
        self.td=td
    def __str__(self):
        return f"{self.mx} {self.tx} {self.h} {self.ms} {self.td} {self.gb}"
class ot(car):
    def __init__(self, mx, tx, h, ms, ml, gb):
        car.__init__(self, mx, tx, h, ms, gb)
        self.ml=ml
    def __str__(self):
        return f"{self.mx} {self.tx} {self.h} {self.ms} {self.ml} {self.gb}"

if __name__=="__main__":
    n=int(input())
    a=[]
    b=[]
    for i in range(1, n+1):
        s=input()
        if s[0]=="X":
            tx=input()
            h=input()
            ms=input()
            td=input()
            gb=int(input())
            a.append(xm(s, tx, h, ms, td, gb))
        elif s[0]=="O":
            tx=input()
            h=input()
            ms=input()
            ml=input()
            gb=int(input())
            b.append(ot(s, tx, h, ms, ml, gb))
    a.sort(key=lambda x: (-x.gb, x.mx))
    b.sort(key=lambda x: (-x.gb, x.mx))
    print("DANH SACH OTO :")
    for item in b:
        print(item)
    print("DANH SACH XE MAY :")
    for item in a:
        print(item)