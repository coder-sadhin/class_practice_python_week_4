def curzon(n):
    one=(2**n)+1
    two=(2*n)+1
    return True if one%two==0 else False
n=int(input())
print(curzon(n))