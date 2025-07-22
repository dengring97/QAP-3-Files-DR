
import datetime

# Constants and values input
HST_RATE = 0.15
LICENCE_FEE_LOW = 75.00
LICENCE_FEE_HIGH = 165.00
TRANSFER_FEE_RATE = 0.01
LUXURY_TAX_RATE = 0.016
MAX_CAR_PRICE = 50000.00
FINANCING_FEE_PER_YEAR = 39.99

# Helper Functions
def format_phone(phone):
    # Accepts 10 digit number as string and returns formatted phone number
    return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"

def get_licence_fee(price):
    return LICENCE_FEE_LOW if price <= 15000 else LICENCE_FEE_HIGH

def get_transfer_fee(price):
    fee = price * TRANSFER_FEE_RATE
    if price > 20000:
        fee += price * LUXURY_TAX_RATE
    return fee

def generate_receipt_id(first_name, last_name, license_plate, phone_number):
    initials = first_name[0].upper() + last_name[0].upper()
    plate_last3 = license_plate[-3:]
    phone_last4 = phone_number[-4:]
    return f"{initials}-{plate_last3}-{phone_last4}"

def get_first_payment_date():
    today = datetime.date.today()
    if today.day >= 25:
        month = today.month + 2
    else:
        month = today.month + 1

    year = today.year
    if month > 12:
        month -= 12
        year += 1
    return datetime.date(year, month, 1)

def calculate_payment_schedule(total_price):
    print("\n--- Payment Schedule (1 to 4 Years) ---")
    for years in range(1, 5):
        months = years * 12
        finance_fee = FINANCING_FEE_PER_YEAR * years
        total_with_financing = total_price + finance_fee
        monthly_payment = total_with_financing / months
        print(f"{years} Year(s): {months} payments of ${monthly_payment:.2f} (includes ${finance_fee:.2f} in fees)")

# Main Program
while True:
    print("\n--- Honest Harry's Used Car Sale Entry ---")

    # Customer First Name
    first_name = input("Enter customer FIRST name (or 'END' to stop): ").strip().title()
    if first_name.upper() == "END":
        break

    # Customer Last Name
    while True:
        last_name = input("Enter customer LAST name (6 characters, format XXX999): ").strip().upper()
        if len(last_name) == 6 and last_name[:3].isalpha() and last_name[3:].isdigit():
            break
        print("Invalid last name. Must be 6 characters in format XXX999.")

    # Phone Number
    while True:
        phone = input("Enter 10-digit phone number (numbers only): ").strip()
        if phone.isdigit() and len(phone) == 10:
            break
        print("Invalid phone number.")

    # Car Details
    make = input("Enter car make (e.g., Toyota): ").strip().title()
    model = input("Enter car model (e.g., Corolla): ").strip().title()
    year = input("Enter car year (e.g., 2018): ").strip()

    # Selling Price
    while True:
        try:
            price = float(input("Enter selling price (max $50,000): $"))
            if 0 < price <= MAX_CAR_PRICE:
                break
            else:
                print("Price must be between $0 and $50,000.")
        except ValueError:
            print("Invalid number.")

    # Trade-In Amount
    while True:
        try:
            trade = float(input("Enter trade-in value (≤ selling price): $"))
            if 0 <= trade <= price:
                break
            else:
                print("Trade-in must not exceed selling price.")
        except ValueError:
            print("Invalid number.")

    # Salesperson
    salesperson = input("Enter salesperson name: ").strip().title()

    # License Plate
    license_plate = input("Enter license plate number: ").strip().upper()

    # Invoice Date
    invoice_date = datetime.date.today()

    # Calculations
    price_after_trade = price - trade
    licence_fee = get_licence_fee(price)
    transfer_fee = get_transfer_fee(price)
    subtotal = price_after_trade + licence_fee + transfer_fee
    hst = subtotal * HST_RATE
    total_price = subtotal + hst

 # Customer and receipt IDs
    customer_id = f"{first_name[0]}{last_name}"

  
    receipt_id = generate_receipt_id(first_name, last_name, license_plate, phone)

    
    first_payment_date = get_first_payment_date()

    # Output Summary
    print("\n--- Invoice Summary ---")
    print(f"Date: {invoice_date}")
    print(f"Customer: {customer_id}")
    print(f"Phone: {format_phone(phone)}")
    print(f"Car: {year} {make} {model}")
    print(f"Salesperson: {salesperson}")
    print(f"Receipt ID: {receipt_id}")
    print(f"Price: ${price:.2f}")
    print(f"Trade-in: -${trade:.2f}")
    print(f"Price After Trade: ${price_after_trade:.2f}")
    print(f"Licence Fee: ${licence_fee:.2f}")
    print(f"Transfer Fee: ${transfer_fee:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"HST (15%): ${hst:.2f}")
    print(f"Total Sales Price: ${total_price:.2f}")
    print(f"First Payment Date: {first_payment_date.strftime('%B %d, %Y')}")

    # Payment Schedule
    calculate_payment_schedule(total_price)
