if __name__ == "__main__":
    expenses = load_expenses()
    add_expense(expenses, "Food", "Rent", "1000")
    add_expense(expenses, "Ingredients", "Bill", 200)
    save_expenses(expenses)
    show_expenses(expenses)