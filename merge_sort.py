import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def measure_merge_sort_time(arr):
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    return end_time - start_time

# Measure time for different input sizes
input_sizes = [1000, 1500, 2500, 5000, 10000]
merge_sort_times = []

for size in input_sizes:
    arr = random.sample(range(size * 10), size)
    sort_time = measure_merge_sort_time(arr)
    merge_sort_times.append((size, sort_time))
    print(f'Merge Sort - Input size: {size}, Time taken: {sort_time:.6f} seconds')
