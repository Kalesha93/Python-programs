print("1. Add")
print("2. Subtract")

choice = int(input("Enter choice: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if choice == 1:
    print("Sum:", a + b)
elif choice == 2:
    print("Difference:", a - b)
else:
    print("Invalid choice")
