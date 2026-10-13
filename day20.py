balance = 5000
pin = 1234
entered_pin = int(input("Enter your ATM PIN: "))
if entered_pin == pin:
    print("\nWelcome to ATM!")
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Your balance is ₹", balance)
        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Money deposited successfully!")
                print("Available balance: ₹", balance)
            else:
                print("Enter a valid amount!")
        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Enter a valid amount!")
            elif amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Available balance: ₹", balance)
            else:
                print("Insufficient balance!")
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice! Try again.")
else:
    print("Incorrect PIN!")

