
def uscln(a, b):
    if(a==b):
        return a
    if(a>b):
        return uscln(a-b, b)
    return uscln(a, b-a)

a = int(input("nhap a: "))
b = int(input("nhap b: "))
print("uscln {} va {} la {}".format(a,b,uscln(a,b)))