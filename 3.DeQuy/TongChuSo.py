def tcs(n):
    if n<10:
        return n%10
    else:
        return n%10+tcs(n//10)

if __name__=='__main__':
    n=int(input())
    print(tcs(n))