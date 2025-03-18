import sys
import datetime
from banker import Banker
from customer import Customer

def display_main_menu():
    print("\nSelect your role:")
    print("1) Banker")
    print("2) Customer")
    print("3) Exit")

def display_banker_menu():
    print("\nBanker Menu:")
    print("1) Add Customer")
    print("2) View Customer")
    print("3) Search Customer")
    print("4) View All Customer")
    print("5) View Total Balance in Bank")
    print("6) Back to Main Menu")

def display_customer_menu():
    print("\nCustomer Menu:")
    print("1) Withdraw Amount")
    print("2) Deposit Amount")
    print("3) View Balance")
    print("4) Back to Main Menu")


def main():
    banker = Banker()
    customer = {} # A dictionary to store customer

    while True:
        display_main_menu()
        try:
            role = int(input("Enter your choice: "))
            if role == 1:   # Banker
                while True:
                    display_banker_menu()
                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        account_number = int(input("Enter Account No: "))
                        name = input("Enter Customer Name: ")
                        balance: float(input("Enter initial balance: "))
                        banker.add_customer(account_number, name, balance)
                        banker.log_transaction(f"{datetime.datetime.now()} - Added Account Number {account_number}: {name}, Balance: {balance}")

                    elif choice == 2:
                        account_number = int(input("Enter Account No. to view: "))
                        banker.view_customer(account_number)

                    elif choice == 3:
                        name = input("Enter customer name to search: ")
                        banker.search_customer(name)

                    elif choice == 4:
                        banker.view_all_customers()

                    elif choice == 5:
                        banker.get_total_balance()

                    elif choice == 6:
                        break   # Back to main menu

                    else:
                        print("Invalid choice. Please try again.")
                
            elif role == 2: # Customer
                account_number = int(input("Enter your Account Number: "))
                if account_number in banker.customers:
                    customer_data = banker.customers[account_number]
                    customer = Customer(account_number, customer_data['name'], customer_data['balance'])

                    while True:
                        display_customer_menu()
                        choice = int(input("Enter Your Choice: "))

                        if choice == 1:
                            amount = float(input("Enter amount to withdraw: "))
                            customer.withdraw(amount)
                            banker.customer[account_number]['balance'] = customer.balance
                            banker.log_transaction(f"{datetime.datetime.now()} - Withdrawn {amount} from Account Number {account_number}")
                        
                        elif choice == 2:
                            amount = float(input("Enter amount to deposit: "))
                            customer.deposit(amount)
                            banker.customers[account_number]['balance'] = customer.balance
                            banker.log_transaction(f"{datetime.datetime.now} - Deposited {amount} into Account Number {account_number}")

                        elif choice == 3:
                            customer.view_balance()

                        elif choice == 4:
                            break   # Back to main menu

                        else:
                            print("Invalid choice. Please try again.")

                else:
                    print("Customer not found.") 

            elif role == 3: # Exit
                print("Exiting the system.")
                sys.exit()

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input, please enter a number.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue

main()