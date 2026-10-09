#http://oj.28tech.com.vn/problem/oop12
class kq:
    def __init__(self, kv, ht, t, l, h):
        self.__kv=kv
        self.__ht=ht
        self.__t=t
        self.__l=l
        self.__h=h
        self.__ut=self.ut()
        self.__sum=self.__t+self.__l+self.__h+self.__ut
    def ut(self):
        if self.__kv[2]=='1':
            return 0.5
        elif self.__kv[2]=='2':
            return 1.0
        elif self.__kv[2]=='3':
            return 2.5
    def dis(self):
        print(self.__kv, self.__ht, self.__kv[2], end=' ')
        if self.__sum%1!=0:
            print('{:.1f}'.format(self.__sum), end=' ')
        else:
            print(int(self.__sum), end=' ')
        if self.__sum>=24:
            print("TRUNG TUYEN")
        else:
            print("TRUOT")
if __name__=="__main__":
    kv=input()
    ht=input()
    t=float(input())
    l=float(input())
    h=float(input())
    a=kq(kv, ht, t, l, h)
    a.dis()
