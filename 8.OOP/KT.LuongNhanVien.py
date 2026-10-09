#http://oj.28tech.com.vn/problem/oop11
class luong:
    def __init__(self, ht, lcb, snc, cv, stt):
        self.__ht=ht
        self.__lcb=lcb
        self.__snc=snc
        self.__cv=cv
        self.__lt=self.__lcb*self.__snc
        self.__pc=self.phuCap()
        self.__th=self.thuong()
        self.__stt=stt
    def phuCap(self):
        if self.__cv=="GD":
            return 250000
        elif self.__cv=="PGD":
            return 200000
        elif self.__cv=="TP":
            return 180000
        elif self.__cv=="NV":
            return 150000
    def thuong(self):
        if self.__snc>=25:
            return (20/100)*(self.__lt)
        elif self.__snc>=22:
            return (10/100)*(self.__lt)
        else:
            return 0
    def __str__(self):
        return f"NV{self.__stt} {self.__ht} {self.__lt} {int(self.__th)} {self.__pc} {self.__lt+self.__pc+int(self.__th)}"
if __name__=="__main__":
    n=int(input())
    for i in range(1, n+1):
        ht=input()
        lcb=int(input())
        snc=int(input())
        cv=input()
        a=luong(ht, lcb, snc, cv, i)
        print(a)