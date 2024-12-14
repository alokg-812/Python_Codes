def b_search(arr, ans):
    low =0
    high = len(arr)-1
    while(high>=low):
        mid = (low+high)//2
        if(arr[mid] == ans):
            return arr[mid]
        elif(arr[mid]>ans):
            high = mid-1
        else:
            low = mid+1
    return -1

arr = [1,4,7,2,3,9,44,8]
arr.sort()
print(arr)
ans = 1

print(b_search(arr, ans))