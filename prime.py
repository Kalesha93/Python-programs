x=int(input("Enter x value"))
y=int(input("Enter y value"))
res = []  

for i in range(x, y + 1):
    if i <= 1:
        continue  
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break 
    else:
        res.append(i)  
print(res if res else "No")
