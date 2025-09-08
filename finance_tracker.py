import csv
from datetime import datetime

FILE_NAME = "finance_data.csv"

# Initialize file if not exists
try:
    open(FILE_NAME, "x").write("Date,Type,Category,Amount,Description\n")
except FileExistsError:
    pass

def add_transaction():
    t_type = input("Enter type (income/expense): ").strip().lower()
    category = input("Enter category (Food, Rent, Salary, etc.): ").strip()
    amount = float(input("Enter amount: "))
    description = input("Enter description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, category, amount, description])

    print("✅ Transaction added successfully!\n")

def view_summary():
    income, expense = 0, 0
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["Amount"])
            if row["Type"] == "income":
                income += amount
            elif row["Type"] == "expense":
                expense += amount
    balance = income - expense
    print(f"\n📊 Summary:")
    print(f"   Total Income:  ₹{income}")
    print(f"   Total Expense: ₹{expense}")
    print(f"   Balance:       ₹{balance}\n")

def view_all_transactions():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        print("\n📑 All Transactions:")
        for row in reader:
            print(f"{row['Date']} | {row['Type']} | {row['Category']} | ₹{row['Amount']} | {row['Description']}")
    print()

def main():
    while True:
        print("====== PERSONAL FINANCE TRACKER ======")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. View All Transactions")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            view_all_transactions()
        elif choice == "4":
            print("👋 Exiting. Your data is saved in finance_data.csv")
            break
        else:
            print("❌ Invalid choice. Try again!\n")

if __name__ == "__main__":
    main()
