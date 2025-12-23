contacts = {}

while True:
    print("\n1.Add  2.View  3.Search  4.Exit")
    ch = input("Choice: ")

    if ch == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif ch == '2':
        print(contacts)
    elif ch == '3':
        name = input("Enter name: ")
        print("Phone:", contacts.get(name, "Not found"))
    else:
        break
