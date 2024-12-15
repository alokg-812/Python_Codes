def pair_sum(L):
    cnt = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if (L[i] + L[j] > 0 and L[i] != L[j]):
                cnt += 1
    return cnt

list = [1,2,3,4,5,-8,-9,-10]
print(pair_sum(list))