# Creating tuple
mobile_brand=("Mi",'Redmi','Samsung','Oppp','Vivo','Google','Motorola','OnePlus','iPhone')
print (type(mobile_brand))
print(mobile_brand)

# read items from list
mobile_brand=("Mi",'Redmi','Samsung','Oppp','Vivo','Google','Motorola','OnePlus','iPhone')
print("Reading by index 1: ",mobile_brand[1])

# reading by for loop
mobile_brand=("Mi",'Redmi','Samsung','Oppp','Vivo','Google','Motorola','OnePlus','iPhone')
for i in mobile_brand:
    print(i,"\t", end="")

# adding element
mobile_brand=["Mi",'Redmi','Samsung','Oppp','Vivo','Google','Motorola','OnePlus','iPhone']
mobile_brand.append("Jio")
print(mobile_brand) 

# updaing element # removing element is not allowed in tuple,
# but we can update element by converting tuple to list and list to tuple
# e.g. tuple->list->update tuple->tuple

# Size of tuple
mobile_brand=("Mi",'Redmi','Samsung','Oppp','Vivo','Google','Motorola','OnePlus','iPhone')
print("No of elements in mobile_brand tuple: ",len(mobile_brand))

# delete tuple
mobile_brand=("Mi",'Redmi','Samsung','Oppp','Vivo','Google','Motorola','OnePlus','iPhone')
print("Before delete: ", mobile_brand)
del mobile_brand
print("After delete: ", mobile_brand)
