import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def measure_bubble_sort_time(arr):
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    return end_time - start_time

# Measure time for different input sizes
input_sizes = [1000, 1500, 2500, 5000, 10000]
bubble_sort_times = []

for size in input_sizes:
    arr = random.sample(range(size * 10), size)
    sort_time = measure_bubble_sort_time(arr)
    bubble_sort_times.append((size, sort_time))
    print(f'Bubble Sort - Input size: {size}, Time taken: {sort_time:.6f} seconds')

