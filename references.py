import sys


class Test:
    pass

x = Test()


reference1 = x
reference2 = reference1


print (" the reference of x", sys.getrefcount(x)) 

del x

print( " There reference of reference1" , sys.getrefcount(reference1))

del reference1

print(" for reference2 reference", sys.getrefcount(reference2))

del reference2

print(" all references deleted")