# Ten Dollar Challenge - OOP Based Console App

class Expense:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount

    def __str__(self):
        return f"{self.title}: ${self.amount:.2f}"

class BudgetTracker:
    def __init__(self, daily_limit=10.0):
        self.daily_limit = daily_limit
        self.expenses = []

    def add_expense(self, expense):
        if self.get_total_spent() + expense.amount <= self.daily_limit:
            self.expenses.append(expense)
            return True
        else:
            return False

    def get_total_spent(self):
        return sum(e.amount for e in self.expenses)

    def get_remaining_budget(self):
        return self.daily_limit - self.get_total_spent()

    def list_expenses(self):
        return self.expenses

    def reset(self):
        self.expenses = []

def main():
    tracker = BudgetTracker()

    while True:
        print("\n==== Ten Dollar Challenge ====")
        print(f"Total Spent: ${tracker.get_total_spent():.2f}")
        print(f"Remaining: ${tracker.get_remaining_budget():.2f}")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Reset Day")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter item name: ")
            try:
                amount = float(input("Enter amount: $"))
                expense = Expense(title, amount)
                if tracker.add_expense(expense):
                    print("✅ Expense added.")
                else:
                    print("❌ Not enough budget left!")
            except ValueError:
                print("❌ Invalid amount. Try again.")
        elif choice == "2":
            print("\n--- Expenses ---")
            for exp in tracker.list_expenses():
                print(exp)
        elif choice == "3":
            tracker.reset()
            print("✅ Budget reset.")
        elif choice == "4":
            print("👋 Exiting. Stay within your $10 budget!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
