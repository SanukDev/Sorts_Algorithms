arr = [5,2,3,7,4,8,6]

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            num = arr[i]
            arr[i] = arr[j]
            arr[j] = num
        print(arr)