import os
import json

def load_data():
    if os.path.exists("budget_data.json"):
        with open("budget_data.json", "r") as file:
            data = json.load(file)
    else:
        data = {"income": 0, "expenses": []}
    return data

def save_data(data):
    with open("budget_data.json", "w") as file:
        json.dump(data, file)

def get_income():
    return float(input("Enter income amount: $"))

def add_income(data):
    income = get_income()
    data["income"] += income
    print(f"Income of ${income} added successfully!")

def get_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: $"))
    return {"name": name, "amount": amount}

def add_expense(data):
    expense = get_expense()
    data["expenses"].append(expense)
    print(f"Expense '{expense['name']}' of ${expense['amount']} added successfully!")

def calculate_budget(data):
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    budget = data["income"] - total_expenses
    return budget

def analyze_expenses(data):
    print("Expense Analysis:")
    for expense in data["expenses"]:
        print(f"{expense['name']}: ${expense['amount']}")

def main():
    data = load_data()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            budget = calculate_budget(data)
            print(f"Current Budget: ${budget}")
        elif choice == "4":
            analyze_expenses(data)
        elif choice == "5":
            save_data(data)
            print("Budget data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
