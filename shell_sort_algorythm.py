arr = [22,34,25,12,64,11,90,88,45]
gap = len(arr) // 2
def insertion_sort(gap, arr):
    i = 0
    while gap + i < len(arr):
        if arr[i] > arr[i+gap]:
            num = arr[i]
            arr[i] = arr[i+gap]
            arr[i+gap] = num
        print(arr)
        i += 1
while gap > 0:

    insertion_sort(gap,arr)
    gap = gap //2
