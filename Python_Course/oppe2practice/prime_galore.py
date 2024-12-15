def prime_numbers(n):
    if n<2:
        return 0
    cnt = 0
    for i in range(2, n):
        if n%i==0:
            return 0
    return 1
    
def prime_galore(lst):
    ans =0
    print("Prime elements at prime indices: ", end="")
    for i in range(len(lst)):
        if prime_numbers(i) and prime_numbers(lst[i]):
            ans+=1
            print(lst[i], end=" ")
    return ans
list = [1,3,11,18,17,23,6,8,10]
print("\n", prime_galore(list))
