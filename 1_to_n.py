n = int(input("Enter n: "))
# def call(n):
#     if n==1: return 1
#     else:
#         call(n-1)
for i in range(n) :
    for j in range(1,n+1):
        print(j,end=" ")
    print('\n')