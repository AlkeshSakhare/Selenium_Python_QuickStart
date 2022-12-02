# # approach 1 by import
# import module_a

# module_a.sum_a(20, 20)

# # approach 2 by from
# from module_a import mul_a

# mul_a(20, 30)


# # approach 3 by -> If both module has same functions then latested imported modules function will be invoke
# from module_b import *
# from module_a import *

# sum_a(20, 40)  # module_a's sum_a is invoked-> Module a 60
