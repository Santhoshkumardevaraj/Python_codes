print('\nGiven a string and an integer number n, remove characters from a string starting from zero up to n and return a new string')

strvar=str(input('Enter any string: '))
intslice=int(input('Enter number to slice: '))

if intslice<len(strvar):
    print(strvar[intslice:])
