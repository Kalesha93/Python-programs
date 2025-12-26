def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so it contains actual position
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy output to arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)

    # Apply counting sort for each digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)

radix_sort(arr)
print("Sorted array:", arr)
