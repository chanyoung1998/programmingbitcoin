import ecc
from helper import run
from ecc import Point,FieldElement

prime = 223
a = FieldElement(0,prime)
b = FieldElement(7,prime)

p = Point(FieldElement(15,prime),FieldElement(86,prime),a,b)
n = 1
while p != Point(None,None,a,b):
    p = n*p
    n += 1

print(n-1)





