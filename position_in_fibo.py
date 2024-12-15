# write a function that accepts a Fibonacci string as argument and returns its position in the sequence
def fibo(n):
    if n == 1:
        return 'a'
    elif n == 2:
        return 'b'
    else:
        return fibo(n-2) + fibo(n-1)

def inverse(s):
    for i in range(1, 100):
        if fibo(i) == s:
            return i
    return -1  # Return -1 if not found

str = input("Enter the Fibonacci-like string: ")
print(inverse(str))
