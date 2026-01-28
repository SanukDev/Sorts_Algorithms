arr = [5,2,3,7,4,8,6]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            num = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = num
            break
        print(arr)