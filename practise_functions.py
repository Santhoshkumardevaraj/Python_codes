# -*- coding: utf-8 -*-

def sum(a,b):
    c=a+b

def sumwithreturn(a,b):
    return a+b

val1=int(input('Enter element1: '))
val2=int(input('Enter element2: '))
print('result',sumwithreturn(val1,val2))
#call by reference in python
#Types of arguments 1 Required 2 keyword 3 default 4 variable length

#required arguments
def sum_required_arguments(a,b):
    return a+b

#default arguments
def sum_default_arguments(a,b=3):
    return a+b

#keyword arguments
def sum_keyword_arguments(a,b):
    return a+b
print('result',sum_keyword_arguments(a=5,b=6))

#variable lenght arguments
def sum_variable_arguments(*a):
    return a
print('result',sum_variable_arguments(1,2,3,4,5,6))