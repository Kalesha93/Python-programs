a = [10, 24, 76, 23, 12]

res = a[0]
for n in a:
    if n > res:
        res = n
print(res)
