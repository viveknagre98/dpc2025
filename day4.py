def merge_sorted_arrays(arr1, arr2):
m = len(arr1)
n = len(arr2)

 i = m - 1  
 j = 0      
    while i >= 0 and j < n:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1
    arr1.sort()
    arr2.sort()

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merge_sorted_arrays(arr1, arr2)

print("arr1 after merge:", arr1)
print("arr2 after merge:", arr2)