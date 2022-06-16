_List1=[1,2,3,4,5,6,7,8,9,0]
_List2=['a',100,'b',200,'c',300]
_List3=[]

print(_List1==_List2)
print(type(_List1))
print(_List1[3])
print(_List1[2:8:2]) #start:stop:step
print(_List1[-5:-2])
print(_List1[-2:-5])
_List1[3]=24
_List1[8:9]=[17,21]
print(_List1)
#LIST OPERATIONS
print('LIST OPERATIONS')
print(_List1*2) #Repetition
print(_List1+_List2)#Concatenation
print(_List2 in _List1) #Membership
print(len(_List1)) #Length
print('LIST ITERATIONS');
for i in range(0,len(_List1)):
    print(i,_List1[i])
print('ADD Elements to the list2')
_List2.append(input('Enter element to add:'))
print(_List2)
print('Remove Elements from the list1')
_List1.remove(2)
print(_List1)
print('List max value',max(_List1))
print('List min value',min(_List1)) #list value should be of same type eg:all int/decimal
print('convert any sequence to list')
teststring="teststring"
print(list(teststring))
