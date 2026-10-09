def sumEven(n):
    if n<10 and n%2==0:
        return n
    else:
        if n%10%2==0:
            return n%10+sumEven(n//10)
        else:
            return sumEven(n//10)
    
def sumOdd(n):
    if n<10 and n%2!=0:
        return n
    else:
        if n%10%2!=0:
            return n%10+sumOdd(n//10)
        else:
            return sumOdd(n//10)
if __name__=='__main__':
    n=int(input())
    print(sumEven(n))
    print(sumOdd(n))
