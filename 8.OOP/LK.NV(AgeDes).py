#http://oj.28tech.com.vn/problem/oop26
class nv:
    def __init__(self, stt, ht, gt, ntns, dc, mst, nkhd):
        self.stt=stt
        self.ht=ht
        self.gt=gt
        self.ntns=ntns
        if self.ntns[1]=='/':
            self.ntns='0'+self.ntns
        if self.ntns[4]=='/':
            self.ntns=self.ntns[0:3:]+'0'+self.ntns[3::]
        self.day, self.month, self.year=map(int, self.ntns.split('/'))
        self.dc=dc
        self.mst=mst
        self.nkhd=nkhd
        if self.nkhd[1]=='/':
            self.nkhd='0'+self.nkhd
        if self.nkhd[4]=='/':
            self.nkhd=self.nkhd[0:3:]+'0'+self.nkhd[3::]
    def __str__(self):
        return f"{'{:05d}'.format(self.stt)} {self.ht} {self.gt} {self.ntns} {self.dc} {self.mst} {self.nkhd}"
if __name__=="__main__":
    m=int(input())
    a=[]
    for i in range(1, m+1):
        ht=input()
        gt=input()
        ntns=input()
        dc=input()
        mst=input()
        nkhd=input()
        a.append(nv(i, ht, gt, ntns, dc, mst, nkhd))
    a.sort(key=lambda x:(x.year, x.month, x.day))
    for item in a:
        print(item)
        