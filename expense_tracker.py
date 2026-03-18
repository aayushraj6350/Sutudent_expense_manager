import csv
from datetime import datetime

while True:
    print("\n====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        note = input("Enter note: ")
        date = datetime.now().strftime("%Y-%m-%d")

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("✅ Expense added successfully!")

    elif choice == "2":
        print("\n📄 Your Expenses:\n")
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    elif choice == "3":
        print("👋 Exiting program. Bye!")
        break

    else:
        print("❌ Invalid choice, try again")