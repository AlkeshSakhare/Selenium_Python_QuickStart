a = 10
try:
    print(5/a)
except ValueError:
    print("this is ValueError exception: ")  # if a value is not supplied
except ZeroDivisionError:
    print("This is divide by exception")  # if a =0
else:
    print("this is me if exception not present")  # if a is integer
