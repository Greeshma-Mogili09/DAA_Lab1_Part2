def print_sorted_lists(sorted_lists):
    sorted_lists = [sorted(lst) for lst in sorted_lists]
    
    for i, sublist in enumerate(sorted_lists):
        print(f"Sorted List {i + 1}: {sublist}")
        
num_lists = int(input("Enter the number of sorted lists/arrays: "))
num_elements = int(input("Enter the number of elements in each list/array: "))

sorted_lists = []
for i in range(num_lists):
    sublist = [int(x) for x in input(f"Enter {num_elements} elements separated by space for List {i + 1}: ").split()]
    sorted_lists.append(sublist)

print_sorted_lists(sorted_lists)
