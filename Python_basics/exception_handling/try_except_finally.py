no = 4
try:
    print(4/no)
except ZeroDivisionError:
    print("Im executed if ZeroDivisionError exception occured")  # if no=0
except:
    # if line 1 is commented
    print("Im executed for exception other than ZeroDivisionError occured")
finally:
    print("Im always executed")
