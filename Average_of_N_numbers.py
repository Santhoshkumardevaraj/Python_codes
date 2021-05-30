print('Average of N nummbers')
int_noe=int(input('Enter number of elements: '))

num=[]

for i in range(0,int_noe):
    print('enter the ',i+1,' number')
    num.insert(i,int(input()))

print('Average: ',sum(num)/len(num))
