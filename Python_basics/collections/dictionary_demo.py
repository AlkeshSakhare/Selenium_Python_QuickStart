emp = {"name": "Teddy",
       "age": 20,
       "color": "red"}

# getting dictionary
print("Type of emp: ", type(emp))
print("Printing emp: ", emp)

# accessing values from key
print("accessing age by get(): ", emp.get("age"))
print("accessing age by []: ", emp["age"])

# length of dictionary
print("length of dictionary using len(): ", len(emp))

# updating value
print("accessing age before update: ", emp["age"])
emp["age"] = 21  # updating value
print("accessing age after update: ", emp["age"])
