import decimal
from fractions import Fraction

print(decimal.Decimal(1)/decimal.Decimal(7))

decimal.getcontext().prec=4


print(decimal.Decimal(1)/decimal.Decimal(7))
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

x=Fraction(1,3)
y=Fraction(4,6)

print(x)
print(y)

print(x+y)
print(x-y)
print(x*y)

print((2.5).as_integer_ratio())
f=2.5
z=Fraction(*f.as_integer_ratio())
print(z)


