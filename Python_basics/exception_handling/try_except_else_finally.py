'''
try: put your code which will generate exception
except <exception> : if specific exception occured then will execute
except : if exception occured and no matched exception is present then will execute
else : if exception is not occured then it will execute
finally : it will always execute
'''

no = 4
'''
1.0
This will execute if exception/error not occured
This will always execute
'''

no = 0
'''
This is ZeroDivisionError
This will always execute
'''

no = a
'''
This is ZeroDivisionError
This will always execute
'''

try:
    print(40/no)
except ZeroDivisionError:
    print("This is ZeroDivisionError")
except:
    print("This will execute if ValueError is not occured")
else:
    print("This will execute if exception/error not occured")
finally:
    print("This will always execute")
