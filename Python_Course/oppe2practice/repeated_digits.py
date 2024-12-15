d = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
n = int(input())
for i in range(1,n+1):
    for j in str(i):
        d[int(j)] += 1
print(d)