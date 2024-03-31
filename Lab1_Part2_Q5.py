def merge_intervals(intervals):
    
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged_intervals = [sorted_intervals[0]]
    
    for interval in sorted_intervals[1:]:
        current_start, current_end = interval
        last_start, last_end = merged_intervals[-1]
        
        
        if current_start <= last_end:
            merged_intervals[-1] = (last_start, max(last_end, current_end))
        else:
            merged_intervals.append(interval)
    
    return merged_intervals

intervals = []
num_intervals = int(input("Enter the number of intervals: "))
for i in range(num_intervals):
    start_time = int(input(f"Enter start time for interval {i+1}: "))
    end_time = int(input(f"Enter end time for interval {i+1}: "))
    intervals.append((start_time, end_time))


merged_intervals = merge_intervals(intervals)


print("Non-overlapping intervals after merging:")
for interval in merged_intervals:
    print(f"Interval: Start time - {interval[0]}, End time - {interval[1]}")
