def max_activities(activities):
    
    sorted_activities = sorted(activities, key=lambda x: x[1])
    max_count = 0
    last_finish_time = float('-inf')
    selected_activities = []
    
    for activity in sorted_activities:
        start_time, finish_time = activity
        
        if start_time >= last_finish_time:
            max_count += 1
            last_finish_time = finish_time
            selected_activities.append(activity)
    
    return max_count, selected_activities


activities = []
num_activities = int(input("Enter the number of activities: "))
for i in range(num_activities):
    start_time = int(input(f"Enter start time for activity {i+1}: "))
    finish_time = int(input(f"Enter finish time for activity {i+1}: "))
    activities.append((start_time, finish_time))


max_count, selected_activities = max_activities(activities)

print("Maximum number of activities:", max_count)
print("Selected activities with start and end times:")
for activity in selected_activities:
    start_time, finish_time = activity
    print(f"Activity: Start time - {start_time}, End time - {finish_time}")
