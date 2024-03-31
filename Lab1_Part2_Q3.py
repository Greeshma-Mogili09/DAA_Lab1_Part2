import heapq

def find_k_largest(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap

nums = list(map(int, input("Enter the array elements separated by space: ").split()))

k = int(input("Enter the value of K: "))

result = find_k_largest(nums, k)
print("K largest elements:", result)
