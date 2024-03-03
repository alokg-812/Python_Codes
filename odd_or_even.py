def Odd_Even(x):
    if(x%2 == 0 ):
        return "EVEN"
    else:
        return "ODD"

a = int(input("Enter the number: "))
print(Odd_Even(a))