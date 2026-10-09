#http://oj.28tech.com.vn/problem/oop09
class luong:
    def __init__(self, mn, ht, lcb):
        self.__mn=mn
        self.__ht=ht
        self.__lcb=lcb
        self.__l=self.tinhLuong()
    def tinhLuong(self):
        if mn[0:2:1]=="HT":
            l=2000000+lcb*(int(mn[2::]))
        elif mn[0:2:1]=="HP":
            l=900000+lcb*(int(mn[2::]))
        elif mn[0:2:1]=="GV":
            l=500000+lcb*(int(mn[2::]))
        return l
    def __str__(self):
        return f"{self.__mn} {self.__ht} {int(self.__mn[2::])} {self.__l}"
if __name__=="__main__":
    mn=input()
    ht=input()
    lcb=int(input())
    a=luong(mn, ht, lcb)
    print(a)