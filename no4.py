def f(a, b):
    result=0
    i=1
    while True:
        if(b*i)>a and (b*i)>b:
            result=b*i
            break
        i+=1
    return int(result)
        

s=input()
new=s.split(",")
a=float(new[0])
b=float(new[-1])
print(f(a,b))