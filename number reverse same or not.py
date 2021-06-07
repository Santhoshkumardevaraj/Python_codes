print('\nReverse a given number and return true if it is the same as the original number')

var_inp=int(input('Enter any number: '))

var_reversed=int(str(var_inp)[::-1])

if var_inp==var_reversed:
    print('same')
else:
    print('not same')
