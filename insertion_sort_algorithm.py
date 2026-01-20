arr = [5,2,3,7,4,8,6]
cont = 1
for i in range(1,len(arr)):
    print(arr)
    cont = i
    print(cont)
    while arr[cont] < arr[cont-1]:
        num = arr[cont-1]
        arr[cont-1] = arr[cont]
        arr[cont] = num
        cont -= 1
        if cont == 0:
            break


print(arr)