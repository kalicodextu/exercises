D={'a':1}
print(D)
print(type(D))

list1=[0,0,0,0,0]
list2=[0]*5
list3=[0 for i in range(5)]

print(list1,list2,list3)

dict1=dict(a=0,b=0)
dict2=dict([('a',0),('b',0)])
dict3=dict.fromkeys(['a','b'],0)
print(dict1,dict2,dict3)

list_test=[]
list_test.append(1)
list_test[0]=2

dict_test={}
dict_test.add('a',1)
print(dict_test)
