def disarium(a):
    result=0
    pw=1
    for char in (a):
        n=int(char)
        result += n**pw
        pw+=1
    return True if result==int(a) else False
a=input()
print(disarium(a))