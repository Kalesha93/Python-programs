def activity_selection(start, finish):
    n = len(start)
    
    print("Selected activities:")
    
    # First activity is always selected
    i = 0
    print(f"Activity {i} (Start: {start[i]}, Finish: {finish[i]})")
    
    # Select remaining activities
    for j in range(1, n):
        if start[j] >= finish[i]:
            print(f"Activity {j} (Start: {start[j]}, Finish: {finish[j]})")
            i = j

# Example input (already sorted by finish time)
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

activity_selection(start, finish)
