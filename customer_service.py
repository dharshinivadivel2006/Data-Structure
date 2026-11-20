# Customer Service System using Queue

customers = []

def add_customer():
    name = input("Enter customer name: ")
    issue = input("Enter customer issue: ")

    customer = {
        "name": name,
        "issue": issue
    }

    customers.append(customer)
    print("\nCustomer added successfully!")

def view_customers():
    if not customers:
        print("\nNo pending customers.")
    else:
        print("\nPending Customers:")
        for customer in customers:
            print("Name:", customer["name"])
            print("Issue:", customer["issue"])
            print("--------------------")

def serve_customer():
    if not customers:
        print("\nNo customers to serve.")
    else:
        customer = customers.pop(0)
        print("\nNow Serving:")
        print("Name:", customer["name"])
        print("Issue:", customer["issue"])

while True:
    print("\n===== CUSTOMER SERVICE SYSTEM =====")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Serve Customer")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        view_customers()
    elif choice == "3":
        serve_customer()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
