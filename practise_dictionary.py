# -*- coding: utf-8 -*-

_dictionary1={"key1":"value1","key2":"value2","key3":12}
_dictionary2=dict({1:"a",2:"b",3:"c"})
print(type(_dictionary1))
print(_dictionary2)
print(_dictionary1["key2"])
_dictionary1['key4']=34
_dictionary2[4]='d'
print(_dictionary1)
print(_dictionary2)
_dictionary1['key2']=53
print(_dictionary1)
del _dictionary1['key2']
print(_dictionary1)
_dictionary1.pop('key1')
print(_dictionary1)
print('\nITERATION\n')

for el in _dictionary2: #print only keys
    print(el)
for el in _dictionary2: #print only values
    print(_dictionary2[el])
for el in _dictionary2.values(): #print only values using values
    print(el)
for el in _dictionary2.items(): #print items
    print(el)
for k,v in _dictionary2.items(): #print items
    print(k,v)

print(len(_dictionary2))
print(_dictionary2.keys())
