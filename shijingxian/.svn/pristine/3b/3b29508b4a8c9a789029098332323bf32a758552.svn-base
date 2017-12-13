import sys


print 'My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform}
data = dict(platform=sys.platform, kind='laptop')
print('My {kind:<8} runs {platform:>8}'.format(**data))
print('My %(kind)-8s runs %(platform)8s' % data)
print('{0:d}'.format(999999999999))
print('{0:,d}'.format(999999999999))
print('{:,d}'.format(999999999999))
print('{:,d} {:,d}'.format(9999999, 8888888))
print('{:,.2f}'.format(296999.2567))
print(bin((2 ** 16)-1))
print '{0:b}'.format((2 ** 16)-1)
print '%s' % bin((2 ** 16)-1)
print('%s' % bin((2 ** 16)-1)[2:])
print('{name} {job} {name}'.format(name='Bob', job='dev'))
print('%(name)s %(job)s %(name)s' % dict(name='Bob', job='dev'))
D=dict(name='Bob',job='dev')
print('{0[name]}{0[job]}{0[name]}'.format(D))
print('{0:f}, {1:.2f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159))
print('%s' % ((1.23,),))
print('%s' % ((1.23,),))
D={}
D['state1']=True
print('state1' in D)
print(D['state1'])

