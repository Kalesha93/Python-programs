correct_username = "Kalesh"
correct_password = "2005"

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Login check
if username == correct_username and password == correct_password:
    print("Login successful ✅")
else:
    print("Invalid username or password ❌")
