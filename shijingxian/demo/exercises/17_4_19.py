import struct

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
'jobs': ['dev', 'mgr'],'age': 40.5}

print(rec)

print(rec['name'])
print(rec['name']['last'])
print(rec['jobs'])
print(rec['jobs'][-1])

rec['jobs'].append('janitor')

print(rec)

D = {'a': 1, 'b': 2, 'c': 3}

D['e']=99
print(D)

print('f' in D)


if not 'f' in D:
    print('missing')
    print('no,really...')

value = D.get('x',0)

print(value)

print(D)

Ks=list(D.keys())
print(Ks)
Ks.sort()
print(Ks)

for key in Ks:
    print(key,'=>',D[key])

for key in sorted(D):
    print(key,'=>',D[key])

for c in 'spam':
    print(c.upper())

X=4
while X>0:
    print('spam!'*X)
    X-=1

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

squares=[]
for x in [1,2,3,4,5]:
    squares.append(x**2)

print(squares)

f=open('data.txt','w')
f.write('Hello\n')
f.write('world\n')
f.close()

f=open('data.txt')
text=f.read()
print(text)


for line in open('data.txt'):
    print(line)

dir(f)


f.close()

X=set('spam')
Y={'h','a','m'}

print(X,Y)
print(X&Y)
print(X|Y)
print(X-Y)
print(X>Y)

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
            return self.name.split()[-1]
    def giveRaise(self, percent):
            self.pay *= (1.0 + percent)

bob=Worker('Bob Smith',50000)
sue = Worker('Sue Jones',60000)

print(bob.lastName())
print(sue.lastName())
sue.giveRaise(.10)
print(sue.pay)

print(15//2.65)






















