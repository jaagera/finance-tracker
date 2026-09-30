import json
import os
DATA_FILE = "expense.json"
def load_expenses():
    """Read expenses from the JSON file. Return an empty list if none exist yet"""
    if not os.path.exists(DATA_FILE):
        RETURN []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


        def save_expenses(expenses):
            """Write the list of expenses to the JSON file."""
            with opne(DATA_FILE, "w") as f:
                json.dump(expenses, f, indent=2)
        
        if __name__ "__main__":
            expense = load_expenses()
            print(f"Loaded {len(expenses)} expenses")