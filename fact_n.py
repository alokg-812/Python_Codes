def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    print(factorial)

x = int(input("Enter the number whose factorial is to be calculated: "))
fact(x)