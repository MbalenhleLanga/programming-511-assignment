account_number = input("Enter account number:")
account_type = input("Enter account type('s' for savings, 'c' for checking):").lower()
minimum_balance = float(input("Enter minimum balance:"))
current_balance = float(input("Enter current balance:"))

if account_type == 's':
    account_name = "Savings"
elif account_type == 'c':
    account_name = "Checking"
else:
    print("Invalid account type!")
    exit()

    if current_balance < minimum_balance:
        if account_type == 's':
            current_balance -= 10.00
            message = "Balance below minimum. Service charge of $10.00 applied."
        else:
            current_balance -= 25.00
            message = "Balance below minimum. Service charge of $25.00 applied."
        else:
if account_type == 's':
    interest = current_balance * 0.04
    current_balance += interest
    message = (f "Interes of ${interest:.2f} (4%) added.")
else:
    excess = current_balance - minimum_balance
    if excess <= 5000:
        interest = current_balance*0.03
        message = f"Interest of ${interest:.2f} (3%) added."
    else:
        interest = current_balance * 0.05
        message = f"Interest of ${interest:.2f} (5%) added."
        current_balance += interest

        print("/n---Account Update Summary---")
        print(f"Account Number: {account_number}")
        print(f"Account Type: {account_name}")
        print(f"Updated Balance: ${current_balance:.2}")
        print(f"Message:{message}")