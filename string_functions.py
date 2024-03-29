str_testvar="this is a test string";

print(str_testvar)
print(len(str_testvar))
print(str_testvar.capitalize())
print(str_testvar.casefold())
print(str_testvar.center(30,'#'))
print(str_testvar.count('is',0,20))
print(str_testvar.encode())
print(str_testvar.startswith('strin',0,len(str_testvar)))
print(str_testvar.endswith('strin',0,len(str_testvar)))
print(str_testvar.find('strin',0,len(str_testvar)))
print("formatted value: {}".format(str_testvar))
print("formatted value: {a}".format(a=str_testvar))
print("formatted value: {1}".format(str_testvar,'test by position'))
print(str_testvar.index('test',0,len(str_testvar))) #same as find, throws error if not found
print(str_testvar.isalnum())
print(str_testvar.isalpha())
print(str_testvar.isdecimal())
print(str_testvar.isdigit())
print(str_testvar.isidentifier())
print(str_testvar.islower())
print(str_testvar.isnumeric())
print(str_testvar.isprintable())
print(str_testvar.isupper())
print(str_testvar.isspace())
print(str_testvar.istitle())
print(str_testvar.join('123'))
print(str_testvar.lstrip())
print(str_testvar.rstrip())
print(str_testvar.replace('t','x',2))
print(str_testvar.split(' ',3))
print(str_testvar.rsplit(' ',3)) # reverse split in backward
print(str_testvar.swapcase())
