a=10# im global variable
print("Global variable",a)

def fun():
    b=4
    print("Local variable",b) # printing local variable
    global a; # accessing gloabl variable
    print(a) # printing global variable
    a=20 # updating global variable value
    print("Global variable value changed in fun()",a)


print("Globle variable value without calling fun()",a) # 10 without calling fun()

fun()
print("Globle variable value after calling fun()",a) # 20 without calling fun()
