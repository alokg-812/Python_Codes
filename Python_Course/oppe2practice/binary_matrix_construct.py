def matrix(H, V):
    if(len(H) != len(V)):
        print("Matrix cannot be formed.")
        return
    else:
        mat = []
        for i in range(len(H)):
            row = []
            for j in range(len(V)):
                if(H[i] % V[j] == 0):
                    row.append(1)
                else:
                    row.append(0)
            mat.append(row)
        return mat

H = [4, 5, 10, 20]
V = [2, 3, 4, 5]
print(matrix(H, V))