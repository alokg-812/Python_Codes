dict1 = {1:2,2:4,3:8,4:16}
dict2 = {1:3,2:9,3:27,4:81}

# print(dict1[2])

for i in range(1, len(dict1)+1):
    print("Sum of 2 and 3 raised to the power "+ str(i)+" is: "+ str( dict1[i]+dict2[i]))
