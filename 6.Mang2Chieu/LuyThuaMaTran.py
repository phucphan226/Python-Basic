mod=10**9+7
class mt:
    def __init__(self, hang, cot, data=None):
        self.hang=hang
        self.cot=cot
        if data==None:
            self.maTran=[[0]*cot for row in range(0, hang)]
        else:
            self.maTran=list(map(list, data))
    def inMang(self):
        for row in self.maTran:
            for item in row:
                print(item, end=" ")
            print()
    def __mul__(self, other):
        kq=mt(self.hang, other.cot)
        for i in range(0, self.hang):
            for j in range(0, other.cot):
                for k in range(0, other.hang):
                    kq.maTran[i][j]+=(self.maTran[i][k]%mod*other.maTran[k][j]%mod)%mod
                    kq.maTran[i][j]%=mod
        return kq
def binPow(a, k):
    if k==1:
        return a
    tam=binPow(a, k//2)
    if k%2==0:
        return tam*tam
    else:
        return tam*tam*a
    
if __name__ == "__main__":  
    n, k=map(int, input().split())
    a=[[0]*n for row in range(0, n)]
    for i in range(0, n):
        a[i]=list(map(int, input().split()))
    a=mt(n, n, a)
    kq=binPow(a, k)
    kq.inMang()

    