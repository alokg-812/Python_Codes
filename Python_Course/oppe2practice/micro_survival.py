# given f(x) = x^2 + y^2- 3x-4y+30
def survival(low, high):
    flag = False
    for i in range(-5,6):
        for j in range(-5,6):
            func = i**2 + j**2 + 3*i + 4*j + 30 
            if (func<=high and func>=low):
                print("{",str(i), ", ", str(j),"}")
                flag = True
        print()
    return flag


low = int(input())
high = int(input())
if(not survival(low, high)):
    print("No possibility of survival")
else:
    print("Possibility of survival")