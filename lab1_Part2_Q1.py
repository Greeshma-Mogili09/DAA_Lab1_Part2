import random
import time
import matplotlib.pyplot as plt

def generate_random_numbers():
    return [random.randint(1, 10000) for _ in range(1000)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


bubble_sort_times = []
insertion_sort_times = []
quick_sort_times = []

sorting_algorithms = [("Bubble Sort", bubble_sort, bubble_sort_times),
                      ("Insertion Sort", insertion_sort, insertion_sort_times),
                      ("Quick Sort", quick_sort, quick_sort_times)]

for _ in range(100):
    numbers = generate_random_numbers()
    for algorithm_name, sorting_function, time_list in sorting_algorithms:
        start_time = time.time()
        sorting_function(numbers.copy())
        time_list.append(time.time() - start_time)


plt.figure(figsize=(10, 6))
for algorithm_name, _, time_list in sorting_algorithms:
    plt.plot(time_list, label=algorithm_name)
plt.xlabel('Iteration')
plt.ylabel('Time (s)')
plt.title('Time Taken for Sorting Algorithms')
plt.legend()
plt.show()
