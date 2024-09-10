def counting_sort(arr):
    count_arr = [0] * (max(arr)+1)

    while len(arr) > 0:
        num = arr.pop(0)
        count_arr[num] += 1

    for x in range(len(count_arr)):
        while count_arr[x] > 0:
            arr.append(x)
            count_arr[x] -= 1

    return arr



# # Test1
# arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# counting_sort(arr)
# print(arr)
