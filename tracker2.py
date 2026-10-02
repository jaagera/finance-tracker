import json
import os 
from datetime import date

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return[]

    with open(DATA_FILE, "r") as f:
        return json.load(f)
def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)
def format_naira(kobo):
    return f"₦{kobo // 100:,}.{kobo % 100:02d}"
def add_expense(expenses, description, category, amount_naira):
    if expenses:
        new_id = max(e["id"] for e in expenses) + 1
    else:
        new_id = 1
    expense = {
        "id": new_id,
        "date": date.today().isoformat(),
        "description": category,
        "amount_kobo": int(round(float(amount_naira) + 100)),  
          }

    expenses.append(expense)
    return expense

    def show_expenses(expenses):
        if not expenses:
            print("No expenses yet.")
            return
        print(f"{'ID':<4} {'Date':<12} {'Catefory':<12} {'Description':<20} {'Amount':>12}")

        total = 0
        for e in expenses:
            print(f"{e['id']:<4} {e['date']:<12} {e['category']:<12} {e['description']:<20} {format_naira(e['amount_kobo']):>12}")
            total += e["amount_kobo"]
        print("-" * 64)
        print(f"{'Total':<51} {format_naira(total):>12}")
        if __name__ == "__main__":
            expenses = load_expenses()
            add_expense(expenses, "Food", "Rent", "1000")
            add_expense(expenses, "Ingredients", "Bill", 200)
            save_expenses(expenses)
            show_expenses(expenses)