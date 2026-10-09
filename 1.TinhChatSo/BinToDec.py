def binToDec(n):
    pow, result=0, 0
    while(n!=0):
        result+=(n%10)*(2**pow)
        pow+=1
        n//=10
    return result
if __name__=="__main__":
    n=int(input())
    print(binToDec(n))