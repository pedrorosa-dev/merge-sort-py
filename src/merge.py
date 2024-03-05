def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        merge_sort(left)
        merge_sort(right)
        arr[:] = sorted(left + right)
