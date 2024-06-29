from datetime import datetime
from validate_email import validate_email
from tabulate import tabulate

# Sets for valid yes and no responses
confirmation_yes = {'y', 'Y', 'Yes', 'yes'}
confirmation_no = {'n', 'N', 'No', 'no'}

# Function to gather user credentials
def get_user_info():
    print('-----------------------------------------')
    print('Please enter the following details:')
    print('-----------------------------------------')
    name = input('Full Name: ')
    address = input('Address: ')
    email = get_valid_email()  # Validate and get email
    province = get_valid_province()  # Validate and get province
    print()
    return name, address, email, province

# Function to validate email address
def get_valid_email():
    while True:
        email = input('Email Address: ')
        if validate_email(email):  # Use validate_email function to check email validity
            return email
        else:
            print("Invalid email address. Please try again.\n")

# Function to validate province
def get_valid_province():
    provinces = {'A': 'LUZON', 'B': 'VISAYAS', 'C': 'MINDANAO'}
    while True:
        print("-----------------------------------------")
        print("Province Options:")
        print("\tA - Luzon")
        print("\tB - Visayas")
        print("\tC - Mindanao")
        print("-----------------------------------------")
        choice = input("Province (A/B/C): ").upper()  # Convert input to uppercase for consistency
        if choice in provinces:
            return provinces[choice]  # Return the full province name
        else:
            print("Please enter a valid option (A, B, or C).\n")

# Function to update user credentials
def update_user_info(name, address, email, province):
    print("-----------------------------------------")
    print("Which information would you like to change?")
    print("\tA - Name")
    print("\tB - Address")
    print("\tC - Email")
    print("\tD - Province")
    print("-----------------------------------------")
    choice = input("> ").upper()  # Convert input to uppercase for consistency
    if choice == 'A':
        name = input('Full Name: ')
    elif choice == 'B':
        address = input('Address: ')
    elif choice == 'C':
        email = get_valid_email()  # Validate and update email
    elif choice == 'D':
        province = get_valid_province()  # Validate and update province
    else:
        print('Invalid choice. Restarting process...')
    print()
    return name, address, email, province

# Function to select a pick-up location based on province
def get_pickup_location(province):
    locations = {
        'LUZON': ["Metro Manila (SM Mall of Asia)", "Baguio (Burnham Park)", "Tagaytay (Sky Ranch)", "Batangas (Laiya Beach)"],
        'VISAYAS': ["Cebu City (Ayala Center Cebu)", "Boracay (Station 2)", "Iloilo City (SM City Iloilo)", "Bacolod (The Ruins)"],
        'MINDANAO': ["Davao City (SM Lanang Premier)", "Cagayan de Oro (Centrio Mall)", "Zamboanga City (Paseo del Mar)", "General Santos City (SM City General Santos)"]
    }
    
    options = locations[province]
    print("-----------------------------------------")
    print("Pick-up Locations:")
    for i, option in enumerate(options, start=1):
        print(f"\t>>> {chr(64+i)} - {option}")
    print("-----------------------------------------")

    while True:
        choice = input("Select a location (A/B/C/D): ").upper()
        if choice in ['A', 'B', 'C', 'D']:
            return options[ord(choice) - 65]  # Convert letter choice to corresponding index
        else:
            print("Invalid choice. Please select a valid option.\n")

# Function to display available cars and their rates
def display_cars():
    cars = [
        [1, "Toyota Vios", '₱2,500.00', '₱3,000.00'],
        [2, "Mitsubishi Mirage", '₱2,300.00', '₱2,800.00'],
        [3, "Honda City", '₱2,800.00', '₱3,300.00'],
        [4, "Toyota Innova", '₱3,500.00', '₱4,000.00'],
        [5, "Ford Everest", '₱4,500.00', '₱5,000.00']
    ]
    print("-----------------------------------------")
    print(tabulate(cars, headers=["Unit", "Model", "Self-Drive (24hrs/d)", "Chauffeur Drive (10hrs/d)"]))
    print("-----------------------------------------")

# Function to select a car and service type
def select_car_and_service():
    while True:
        try:
            car_choice = int(input("Choose a car (1-5): "))
            if car_choice in range(1, 6):
                service_type = input("Service Type (S - Self-Drive / C - Chauffeur): ").upper()
                if service_type in ['S', 'C']:
                    return car_choice, service_type  # Return the selected car and service type
                else:
                    print("Invalid service type. Please enter S or C.")
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get car details based on selection
def get_car_details(car_choice, service_type):
    car_data = {
        1: ["Toyota Vios", "Red", 5, {'S': 2500, 'C': 3000}],
        2: ["Mitsubishi Mirage", "Gray", 5, {'S': 2300, 'C': 2800}],
        3: ["Honda City", "Black", 5, {'S': 2800, 'C': 3300}],
        4: ["Toyota Innova", "Dark Red", 7, {'S': 3500, 'C': 4000}],
        5: ["Ford Everest", "Light Black", 7, {'S': 4500, 'C': 5000}]
    }
    car = car_data[car_choice]
    model, color, seats, rates = car
    price = rates[service_type]
    return model, color, seats, price, 'Self-Driven' if service_type == 'S' else 'Chauffeur'

# Function to get the pick-up date
def get_pickup_date():
    while True:
        try:
            date_str = input("Pick-up date (MM/DD/YYYY): ")
            date = datetime.strptime(date_str, '%m/%d/%Y')
            if date <= datetime.today():
                raise ValueError("Date cannot be today or in the past.")  # Ensure date is in the future
            return date_str
        except ValueError as e:
            print(f"Invalid date: {e}. Please try again.")

# Function to calculate the total rental cost
def calculate_total_cost(price_per_day):
    while True:
        try:
            rental_days = int(input("Number of days to rent: "))
            if rental_days <= 0:
                raise ValueError("Number of days must be positive.")
            total = price_per_day * rental_days  # Calculate total cost based on days and daily rate
            return rental_days, total
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

# Function to handle payment
def process_payment(total_cost):
    while True:
        try:
            print("-----------------------------------------")
            print(f"Total cost: ₱{format(total_cost, ',.2f')}")
            payment = float(input("Enter payment amount: ₱"))
            if payment >= total_cost:
                change = payment - total_cost  # Calculate change if payment is sufficient
                return payment, change
            else:
                print("Insufficient payment. Please enter a sufficient amount.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

# Function to confirm the order before finalizing
def confirm_order():
    print("-----------------------------------------")
    confirmation = input("Would you like to confirm your order? (y/n): ").lower()
    while confirmation not in confirmation_yes.union(confirmation_no):
        print("Invalid input. Please enter 'y' or 'n'.")
        confirmation = input("Would you like to confirm your order? (y/n): ").lower()
    return confirmation in confirmation_yes  # Return True if order is confirmed

# Main program
print("\n╔══════════════════════════════════════════════════════════════╗")
print("║               WELCOME TO PREMIER CAR RENTAL SERVICE!         ║")
print("╚══════════════════════════════════════════════════════════════╝\n")

# Gather user credentials
name, address, email, province = get_user_info()

# Allow user to update credentials if needed
while True:
    change_info = input('Would you like to change any information? (y/n) - ').lower()
    if change_info in confirmation_yes:
        name, address, email, province = update_user_info(name, address, email, province)
    elif change_info in confirmation_no:
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# Choose pick-up location
pickup_location = get_pickup_location(province)

# Display available cars and get user's choice
display_cars()
car_choice, service_type = select_car_and_service()

# Get car details based on user's choice
model, color, seats, price, service = get_car_details(car_choice, service_type)

# Get the pick-up date
pickup_date = get_pickup_date()

# Calculate the total rental cost
rental_days, total_cost = calculate_total_cost(price)

# Process payment
payment, change = process_payment(total_cost)

# Display rental summary
rental_summary = [
    ["Name", name],
    ["Address", address],
    ["Email", email],
    ["Province", province],
    ["Pick-up Location", pickup_location],
    ["Car Model", model],
    ["Car Color", color],
    ["Seats", seats],
    ["Service Type", service],
    ["Pick-up Date", pickup_date],
    ["Number of Days", rental_days],
    ["Total Cost", f'₱{format(total_cost, ",.2f")}'],
    ["Payment", f'₱{format(payment, ",.2f")}'],
    ["Change", f'₱{format(change, ",.2f")}']
]

print("-----------------------------------------")
print("Car Rental Summary")
print(tabulate(rental_summary, headers=["Category", "Details"], tablefmt='grid'))

# Ask for confirmation before finalizing order
if confirm_order():
    print("\n╔════════════════════════════════════════╗")
    print("║  Thank you for choosing our car rental ║")
    print("║      service. Have a safe trip!        ║")
    print("╚════════════════════════════════════════╝\n")
else:
    print("\nOrder not confirmed. You can make changes or cancel anytime.\n")
