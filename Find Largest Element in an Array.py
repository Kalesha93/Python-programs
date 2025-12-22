arr = [10, 324, 45, 90, 9808]
res = arr[0]

for i in range(1, len(arr)):
    if arr[i] > res:
        res = arr[i]

print(res)
