print("list(range(10)): ", list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("list(range(1,10)): ",list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("list(range(1,10,2)): ",list(range(1,10,2))) # [1, 3, 5, 7, 9]
print("list(range(2,10,2)): ",list(range(2,10,2))) # [2, 4, 6, 8]
sum=0
for i in range(1,11):
    sum=sum+i
print("sum of 1st 10 no: ",sum)
