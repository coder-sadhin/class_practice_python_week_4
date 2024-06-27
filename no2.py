# from decimal import Decimal
# def dis(a):
#     new=a.split(",")
#     a=float(new[0])
#     b=float(new[-1])
#     result=a - (a/100)*b
#     return ("%.2f" % result)
# a=input()
# result=dis(a)
# s=str(result)
# if(s[-1]!=0 and s[-2]!=0):
#     s=Decimal(s)
#     print(s)
# else:
#     s=s[:len(s)-1]
#     s=Decimal(s)
#     print(s)

def dis(a):
    new=a.split(",")
    a=float(new[0])
    b=float(new[-1])
    result=a - (a/100)*b
    results=str(result)
    if(results[-1]=='9' or results[-2]=='.'):
        return ("%.1f" % result)
    else:
        return ("%.2f" % result)
a=input()
result=dis(a)
print(result)