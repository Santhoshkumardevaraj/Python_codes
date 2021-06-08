print('\nGiven a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list')

var_list1=[10,15,21,50,55,3]
var_list2=[4,13,22,18,34,41]
var_newlist=[]

for item in var_list1:
    if item%2!=0:
        var_newlist.append(item)
        
for item in var_list2:
    if item%2==0:
        var_newlist.append(item)

print(var_newlist)
