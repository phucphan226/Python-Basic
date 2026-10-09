#http://oj.28tech.com.vn/problem/oop21
class matHang:
    def __init__(self, stt, tmh, dvt, gm, gb):
        self.stt=stt
        self.__tmh=tmh
        self.__dvt=dvt
        self.gm=gm
        self.gb=gb
    def __str__(self):
        return f"MH{'{:04d}'.format(self.stt)} {self.__tmh} {self.__dvt} {self.gm} {self.gb} {self.gb-self.gm}"
if __name__=="__main__":
    m=int(input())
    a=[]
    for i in range(1, m+1):
        tmh=input()
        dvt=input()
        gm=int(input())
        gb=int(input())
        a.append(matHang(i, tmh, dvt, gm, gb))
    a.sort(key=lambda x: (x.gm-x.gb, x.stt))
    for item in a:
        print(item)