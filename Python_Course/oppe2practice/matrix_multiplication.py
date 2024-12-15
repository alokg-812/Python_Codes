def multiply_two_matrices(m1, m2):
    # Ensure valid dimensions for multiplication
    if len(m1[0]) != len(m2):
        raise ValueError("Invalid dimensions for matrix multiplication")
    
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def multiplication_matrix(a,b,c,d,e):
    
    ans = multiply_two_matrices(a, b)
    ans = multiply_two_matrices(ans, c)
    ans = multiply_two_matrices(ans, d)
    ans = multiply_two_matrices(ans, e)
    return ans
# Matrix A
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matrix B
b = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

# Matrix C
c = [
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27]
]

# Matrix D
d = [
    [28, 29, 30],
    [31, 32, 33],
    [34, 35, 36]
]

# Matrix E
e = [
    [37, 38, 39],
    [40, 41, 42],
    [43, 44, 45]
]

# Print matrices
print("Matrix A:", a)
print("Matrix B:", b)
print("Matrix C:", c)
print("Matrix D:", d)
print("Matrix E:", e)
print(multiplication_matrix(a,b,c,d,e))