import random
from collections import namedtuple

Customer = namedtuple('Customer', 'name account_number password phone balance address age DOB account_type')

bank_data = []

def add_customer(name, account_number,password, phone, balance, address, age, DOB, account_type):
    customer = {'name': name, 'account_number': account_number,'password':password ,'phone': phone, 'balance': balance, 'address': address,
                'age': age, 'DOB': DOB, 'account_type': account_type}
    bank_data.append(customer)
    print(f'{customer} \nAdded to the system.\n')

def remove_customer(account_number,password):
    global bank_data
    found = False

    for customer in bank_data:
        if customer['account_number'] == account_number:
            if customer['password'] == password:
                bank_data.remove(customer)
                found = True
                print(f"Customer with account number {account_number} is removed from the system.")
                break


    if not found:
        print("Customer not found.")

def find_customer(account_number,password):
    for customer in bank_data:
        if customer['account_number'] == account_number:
            if customer['password'] == password:
                print(f'Name: {customer["name"]}')
                print(f'Account Number: {customer["account_number"]}')
                print(f'Phone: {customer["phone"]}')
                print(f'Balance: {customer["balance"]}')
                print(f'Address: {customer["address"]}')
                print(f'Age: {customer["age"]}')
                print(f'DOB: {customer["DOB"]}')
                print(f'Account Type: {customer["account_type"]}')
                return

    print("Customer not found.")
def update_balance(account_number, amount, operation):
    for i in range(len(bank_data)):
        customer = bank_data[i]
        if customer['account_number'] == account_number:
            if operation == 'deposit':
                customer['balance'] += amount
                print(f'Balance updated. New balance: {customer["balance"]}')
                return
            elif operation == 'withdraw':
                if customer['balance'] >= amount:
                    customer['balance'] -= amount
                    print(f'Balance updated. New balance: {customer["balance"]}')
                    return
                else:
                    print("Insufficient funds.")
                    return
    print("Customer not found.")
def display_all_customers():
    if not bank_data:
        print("No customer data available.")
        return
    for customer in bank_data:
        print(f'{customer}\n')
names=['Liam', 'John', 'Scarlett', 'Ethan', 'Ella', 'Ava', 'Sarah', 'Madison', 'Victoria', 'Hannah', 'James', 'Sophia', 'Emma', 'Oliver', 'Zoey', 'Sophia', 'Oliver', 'Ethan', 'Victoria', 'Chris', 'Amelia', 'Lily', 'James', 'Henry', 'Mia', 'Madison', 'Zoey', 'Isaac', 'Liam', 'Benjamin', 'Michael', 'Sofia', 'Ethan', 'Daniel', 'Aria', 'Abigail', 'Liam', 'Victoria', 'Andrew', 'Zoey', 'Lucas', 'Noah', 'Jack', 'Benjamin', 'Harper', 'Jack', 'Alexander', 'David', 'Isaac', 'Amelia']


def generate_random_phone_number():
    # Generate the components of the phone number
    area_code = random.randint(100, 999)   # Area code (3 digits)
    first_part = random.randint(100, 999) # First 3 digits
    second_part = random.randint(1000, 9999) # Last 4 digits

    # Format the phone number
    phone_number = f"({area_code}) {first_part}-{second_part}"
    return phone_number


def generate_random_address():
    # Components for the address
    street_names = ["Main St", "Highland Ave", "Maple St", "Broadway", "Elm St", "Park Ave", "Cedar St", "Pine St",
                    "Oak St", "Willow St"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego",
              "Dallas", "San Jose"]
    states = ["NY", "CA", "IL", "TX", "AZ", "PA", "FL", "OH", "GA", "NC"]

    house_number = random.randint(1, 9999)  # Random house number
    street_name = random.choice(street_names)  # Random street name
    city = random.choice(cities)  # Random city
    state = random.choice(states)  # Random state
    zip_code = random.randint(10000, 99999)  # Random ZIP code (5 digits)

    # Combine components into a full address
    address = f"{house_number} {street_name}, {city}, {state} {zip_code}"
    return address
from datetime import datetime, timedelta

def generate_random_dob(start_year=1940, end_year=2023):
    # Generate a random date within the range
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    # Format the date as a string (e.g., "YYYY-MM-DD")
    dob = random_date.strftime("%Y-%m-%d")
    return dob

for i in range(0,50):
    name =names[i]
    account_number = random.randint(50,100)
    password = random.randint(0,1000)
    phone = generate_random_phone_number()
    balance = random.randint(5000,300000)
    address = generate_random_address()
    age = random.randint(18,100)
    DOB = generate_random_dob()
    account_type = 'Savings'

    add_customer(name, account_number,password, phone, balance, address, age, DOB, account_type)

print(bank_data)
x = 0
while x == 0:
    cmd = input('Press: \n 1: To add a new customer \n 2: Remove a customer \n 3: Find customer details \n 4: Display all customer data \n 5: Update balance \n 6: Exit \nEnter: ')

    if cmd == '1':
        name = input('Enter Customer Name: ')
        account_number = int(input('Enter Account Number: '))
        password = int(input('Enter your password'))
        phone = input('Enter Phone Number: ')
        balance = int(input('Enter Initial Balance: '))
        address = input('Enter Address: ')
        age = input('Enter Age: ')
        DOB = input('Enter Date of Birth (DD-MM-YYYY): ')
        account_type = input('Enter Account Type (Savings/Current): ')

        add_customer(name, account_number, password, phone, balance, address, age, DOB, account_type)

    elif cmd == '2':
        account_number = int(input('Enter Account Number to Remove: '))
        password = int(input('Enter your password to remove'))
        remove_customer(account_number,password)


    elif cmd == '3':
        account_number = int(input('Enter Account Number to Search: '))
        password = int(input('Enter your password to search'))
        find_customer(account_number,password)


    elif cmd == '4':
        display_all_customers()

    elif cmd == '5':
        account_number = int(input('Enter Account Number: '))
        password = int(input('Enter your password'))
        operation = input('Enter operation (deposit/withdraw): ').lower()
        if operation not in ['deposit', 'withdraw']:
            print("Invalid operation. Please enter 'deposit' or 'withdraw'.")
            continue
        amount = int(input('Enter amount: '))
        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        update_balance(account_number, amount, operation)

    elif cmd == '6':
        x = 1
        print("Exiting the system.")
