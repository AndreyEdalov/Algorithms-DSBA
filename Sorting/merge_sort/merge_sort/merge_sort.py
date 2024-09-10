def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        
        left_index = 0
        right_index = 0
        main_index = 0
        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] < right_arr[right_index]:
                arr[main_index] = left_arr[left_index]
                left_index += 1
            else:
                arr[main_index] = right_arr[right_index]
                right_index += 1
            main_index += 1
        
        while left_index < len(left_arr):
            arr[main_index] = left_arr[left_index]
            main_index += 1
            left_index += 1
            
        while right_index < len(right_arr):
            arr[main_index] = right_arr[right_index]
            main_index += 1
            right_index += 1
        
arr_test = [45, 12, 78, 3, 89, 23, 56, 34, 90, 11]
merge_sort(arr_test)
print(arr_test)