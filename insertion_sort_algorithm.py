arr = [5,2,3,7,4,8,6]
for i in range(1,len(arr)):
    print(arr)
    if arr[i-1] > arr[i]:
        num = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = num


print(arr)