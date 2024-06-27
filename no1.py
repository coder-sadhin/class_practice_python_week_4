# def triangle(a,b):
#     result=(a*b)/2
#     return result
# a=int(input())
# b=int(input())
# print("%.1f" % triangle(a,b))
def triangle(a):
    new=a.split(",")
    a=int(new[0])
    b=int(new[-1])
    result=(a*b)/2
    print("%.1f" % result)
a=input()
triangle(a)