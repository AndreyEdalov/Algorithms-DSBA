def Insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == "__main__":
    arr = [3,4,1,8,7,6,5]
    Insertion_sort(arr)
    print(*arr)
