print('Given a string, display only those characters which are present at an even index number.')

strvar='programming'
print(strvar)
for i in range(0,len(strvar)):
    if i==0 or i%2==0:
        print(strvar[i],end=" ")
