fibo=[0]*100
def kt():
    fibo[0], fibo[1]=0, 1
    for i in range(2, 100, 1):
        fibo[i]=fibo[i-1]+fibo[i-2]

if __name__=='__main__':
    kt()
    for index in fibo:
        print(index, end=' ')


