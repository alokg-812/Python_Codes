def min_list(l):
    mini = l[0]
    for i in range(len(l)):
        if l[i] < mini:
            mini = l[i]
    return mini

def obvious_sort(l):
    x = []
    while(len(l)>0):
        mini = min_list(l)
        x.append(mini)
        l.remove(mini)
    return x

l = [2, 65, 32, 62, 98, 90]
print(obvious_sort(l))