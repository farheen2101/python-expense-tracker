# main.py
from expense_manager import (
    add_expense, get_all_expenses, get_total_expenses,
    delete_expense, edit_expense, category_summary, monthly_summary
)

def display_expenses():
    expenses = get_all_expenses()
    if not expenses:
        print("No expenses yet.")
    else:
        for i, exp in enumerate(expenses):
            print(f"{i}. Amount: {exp['amount']}, Category: {exp['category']}, Description: {exp['description']}, Date: {exp['date']}")

def main_menu():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Delete Expense")
        print("5. Edit Expense")
        print("6. View Category Summary")
        print("7. View Monthly Summary")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ").strip()
                description = input("Enter description: ").strip()
                date = input("Enter date (YYYY-MM-DD): ").strip()
                add_expense(amount, category, description, date)
                print("✅ Expense added successfully!")
            except ValueError:
                print("❌ Invalid amount.")

        elif choice == "2":
            display_expenses()

        elif choice == "3":
            total = get_total_expenses()
            print(f"💰 Total Expenses: {total}")

        elif choice == "4":
            display_expenses()
            try:
                index = int(input("Enter index of expense to delete: "))
                removed = delete_expense(index)
                if removed:
                    print(f"✅ Deleted: {removed}")
                else:
                    print("❌ Invalid index.")
            except ValueError:
                print("❌ Must enter a number.")

        elif choice == "5":
            display_expenses()
            try:
                index = int(input("Enter index of expense to edit: "))
                amount_input = input("New amount (leave blank to keep current): ").strip()
                category = input("New category (leave blank to keep current): ").strip()
                description = input("New description (leave blank to keep current): ").strip()
                date = input("New date (YYYY-MM-DD, leave blank to keep current): ").strip()
                amount = float(amount_input) if amount_input else None
                updated = edit_expense(index, amount, category or None, description or None, date or None)
                if updated:
                    print(f"✅ Updated: {updated}")
                else:
                    print("❌ Invalid index.")
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "6":
            summary = category_summary()
            if not summary:
                print("No expenses yet.")
            else:
                print("\n💳 Category Summary:")
                for cat, total in summary.items():
                    print(f"{cat}: {total}")

        elif choice == "7":
            summary = monthly_summary()
            if not summary:
                print("No expenses yet.")
            else:
                print("\n📅 Monthly Summary:")
                for month, total in summary.items():
                    print(f"{month}: {total}")

        elif choice == "8":
            print("Exiting…")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()