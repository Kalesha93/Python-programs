import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jumping through the array
    while prev < n and arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search in the block
    while prev < min(step, n):
        if arr[prev] == x:
            return prev
        prev += 1

    return -1


# Example (array must be sorted)
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 13

result = jump_search(arr, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
