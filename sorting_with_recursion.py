def min(L):
    mini = L[0]
    for i in L:
        if i < mini:
            mini = i
    return mini
def sort(L):
    if len(L) == 1 or L == []:
        return L
    else:
        mini = min(L)
        L.remove(mini)
        return [mini] + sort(L)
    

list = [1,4,7,2,3,9,44,8]
print(sort(list))
flag = False