import datetime

class Banker:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name, balance):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.customers[account_number] = {
            'name': name, 
            'balance': balance, 
            'Opening date': current_time
        }
        print(f"Customer {name} added successfully!")

    def view_customer(self, account_number):
        if account_number in self.customers:
            print(f"Customer No: {account_number}")
            for key, value in self.customers[account_number].items():
                print(f"{key}: {value}")
        else:
            print("Customer not found!")

    def search_customer(self, name):
        found = False
        for account_number, details in self.customer.items():
            if details['name'].lower() == name.lower():
                print(f"Account No.: {account_number}")
                for key, value in details.items():
                    print(f"{key}: {value}")
                found = True
        if not found:
            print(f"Customer with name {name} not found!")

    def view_all_customers(self):
        if self.customers:
            print("All Customers:")
            for account_number, details in self.customers.items():
                print(f"\nCustomer ID: {account_number}")
                for key, value in details.items():
                    print(f"{key}: {value}")
        else:
            print("No customers found!")

    def get_total_balance(self):
        total_balance = sum(customer['balance'] for customer in self.customers.values())
        print(f"Total balance in bank: {total_balance}")
        return total_balance

    def log_transaction(self, transaction_details):
        with open('transaction_log.txt', 'a') as log_file:
            log_file.write(transaction_details + '\n')
