_set1={1,2,3,4,5,6,7,8,9,0}
_set2=set([2,4,6,7,'a','b','c','d','e','f','g','h','i','j','k','l',])

print(type(_set1),type(_set2))
print(_set1)
for element in _set2:
    print(element)
_set2.add('January')
print(_set2)
_set2.update(['February','March','April'])
print(_set2)
print("DELETION METHOD")
_set2.discard('e')
print(_set2) # wont show error if not exist
_set2.remove('f')
print(_set2) # show error if not exist
_set2.pop()
print(_set2)# Remove last element from the unordered collection
print(_set1|_set2)#Union operation
print(_set1.union(_set2))#union operation
print(_set1&_set2)#intersection operation
print(_set1.intersection(_set2))#intersection operation
#a.intersection_update(b,c) remove elements from a that is not present in b & c
print('DIFFERENCE')#exist in both sets
print(_set1-_set2)
print(_set1.difference(_set2))
print(_set1.symmetric_difference(_set2))#elements not common in both
_copiedset=_set1.copy()#shallow copy of set1
print(_copiedset)
print(_set1.isdisjoint(_set2))#check is there is null intersection=>true
Frozenset = frozenset([1,2,3,4,5]) #frozenset = immutable sets
print(type(Frozenset))
print(_set1.issubset(_copiedset))#Report whether another set contains this set.
print(_set1.issuperset(_set2))#Report whether this set contains another set.
