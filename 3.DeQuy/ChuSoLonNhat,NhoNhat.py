def findMax(n):
    if n<10:
        return n
    else:
        return int(max(n%10, findMax(n//10)))
def findMin(n):
    if n<10:
        return n
    else:
        return int(min(n%10, findMin(n//10)))

if __name__=='__main__':
    n=int(input())
    print(findMax(n), findMin(n))