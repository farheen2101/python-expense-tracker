from storage import load_data, save_data
from collections import defaultdict
from datetime import datetime

def add_expense(amount, category, description, date):
    expenses = load_data()
    expenses.append({"amount": amount, "category": category, "description": description, "date": date})
    save_data(expenses)

def get_all_expenses():
    return load_data()

def get_total_expenses():
    expenses = load_data()
    return sum(exp["amount"] for exp in expenses)

def delete_expense(index):
    expenses = load_data()
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        save_data(expenses)
        return removed
    return None

def edit_expense(index, amount=None, category=None, description=None, date=None):
    expenses = load_data()
    if 0 <= index < len(expenses):
        if amount is not None: expenses[index]["amount"] = amount
        if category is not None: expenses[index]["category"] = category
        if description is not None: expenses[index]["description"] = description
        if date is not None: expenses[index]["date"] = date
        save_data(expenses)
        return expenses[index]
    return None

# Level 2 function — this is your code
def category_summary():
    """
    Returns total amount spent per category.
    Example: {'Food': 1200, 'Transport': 800}
    """
    expenses = load_data()
    summary = defaultdict(float)
    for exp in expenses:
        summary[exp['category']] += exp['amount']
    return dict(summary)

def monthly_summary():
    expenses = load_data()
    summary = defaultdict(float)
    for exp in expenses:
        try:
            month = datetime.strptime(exp['date'], "%Y-%m-%d").strftime("%Y-%m")
            summary[month] += exp['amount']
        except ValueError:
            continue
    return dict(summary)