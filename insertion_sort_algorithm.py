arr = [22,34,25,12,64,11,90,88,45]
cont=0
for i in range(len(arr) -1):
    for j in range(cont):
        if arr[j] > arr[i+1]:
            num = arr[j]
            arr[j] = arr[i+1]
            arr[i+1] = num
    cont += 1