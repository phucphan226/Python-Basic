class hs:
    def __init__(self, stt, ht, dtb):
        self.stt=stt
        self.ht=ht
        self.dtb=dtb
    def dis(self):
        print("HS", '{:02d}'.format(self.stt), sep='', end=' ')
        print(self.ht, '{:.1f}'.format(self.dtb), end=' ')
        if self.dtb>=9:
            print("XUAT SAC")
        elif self.dtb>=8:
            print("GIOI")
        elif self.dtb>=7:
            print("KHA")
        elif self.dtb>=5:
            print("TB")
        else:
            print("YEU")

if __name__=="__main__":
    m=int(input())
    a=[]
    for i in range(1, m+1):
        ht=input()
        d1, d2, d3, d4, d5, d6, d7, d8, d9, d10=map(float, input().split())
        dtb=(d1+d2+d3+d4+d5+d6+d7+d8+d9+d10)/10
        a.append(hs(i, ht, dtb))
    a.sort(key=lambda x: -x.dtb)
    for item in a:
        item.dis()
