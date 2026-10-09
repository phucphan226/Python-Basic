count=[0]*1000000
def init(a, n):
    b=set()
    for i in range(n-1, -1, -1):
        b.add(a[i])
        count[i]=len(b)

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    l=int(input())
    print(count[l])

