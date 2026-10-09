class net:
    def __init__(self, tk, mk, ht, bd, kt):
        self.tk=tk
        self.mk=mk
        self.ht=ht
        self.bd=bd
        a, b=map(int, self.bd.split(':'))
        self.kt=kt
        c, d=map(int, self.kt.split(':'))
        self.minute=c*60+d-a*60-b
    def __str__(self):
        return f"{self.tk} {self.mk} {self.ht} {self.minute//60} gio {self.minute%60} phut"
if __name__=="__main__":
    n=int(input())
    a=[]
    for i in range(1, n+1):
        tk=input()
        mk=input()
        ht=input()
        bd=input()
        kt=input()
        a.append(net(tk, mk, ht, bd, kt))
    a.sort(key=lambda x: (-x.minute, x.tk))
    for item in a:
        print(item)
