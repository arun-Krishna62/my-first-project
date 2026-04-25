balance = 1000

print("Welcome to ATM!")
print(f"Your balance: {balance}")
choice = input("\n1. Deposit\n2.Withdraw\n3. Check Balance\nEnter choice: ")
if choice == "1":
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print(f"Deposited! New balance: {balance}")


elif choice == "2":
    amount = int(input("Enter withdraw amount: "))
    if amount > balance:
        print("insufficient balance!")
    else:
        balance = balance - amount
        print(f"Withdrawn! New balance: {balance}")

elif choice == "3":
    print(f"Your balance: {balance}")

else:
    print("invalid choice!")