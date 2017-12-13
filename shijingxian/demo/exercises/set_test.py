



x=set('abcde')
y=set('bdxyz')

print(x)
print(x-y)

print(x|y)
print(x&y)
print(x^y)

print(x>y,x<y)
print('e' in x)
print('e' in 'Camelot',22 in [11,22,33])

z=x.intersection(y)
print(z)
z.add('spam')
print(z)
z.update(set(['X','Y']))
print(z)
z.remove('b')
print(z)
for item in set('abc'):
    print(item*3)

S=set([1,2,3])
print S|set([3,4])
#S|[3,4]
print S.union([3,4])
print S.intersection((1,3,4))

print S.issubset(range(-5,5))
s=set({1.23})
try:
    s.add([1,2,3])
except TypeError:
    print 'TypeError Occored!'
finally:
    pass

try:
    s.add({'a':1})
except TypeError:
    print 'TypeError Occored!'
finally:
    pass

try:
    s.add((1,2,3))
except Exception:
    print('Exception Occored!')
finally:
    pass
print s
print s|{(4,5,6),(1,2,3)}
print((1,2,3) in s)
print((1,4,3) in s)





