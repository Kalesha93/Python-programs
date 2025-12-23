balance = 0

while True:
    print("\n1.Deposit  2.Withdraw  3.Balance  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        amt = int(input("Enter amount: "))
        balance += amt
        print("Amount deposited")
    elif ch == 2:
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            print("Amount withdrawn")
        else:
            print("Insufficient balance")
    elif ch == 3:
        print("Balance:", balance)
    else:
        break
