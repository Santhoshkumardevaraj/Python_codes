print('\nGiven a list of numbers, Iterate it and print only those numbers which are divisible of 5')

var_list=[12,15,16,21,20,35,10]

print(var_list)

print('\ndivisble by 5:')

for item in var_list:
    if item%5==0:
        print(item,end="\t")
