import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class Expense:
        def __init__(self, date, description, amount, category):
            self.amount = amount
            self.date = date
            self.description = description
            self.category = category
class ExpenseTracker:
        def __init__(self):
          self.expenses = []
        
        def add_expense(self,expense):
          self.expenses.append(expense)
        
        def remove_expense(self,index):
            if 0 <= index < len(self.expenses):
                self.expenses.pop(index)
            else:
                print("Invalid index")
        def view_expenses(self):
            if len(self.expenses) == 0:
                print("No expenses to show")
            else:
                for i,expense in enumerate(self.expenses, start = 1):
                    print(f"{i}. Date:  {expense.date} | Description : {expense.description} | Amount : ${expense.amount} | Category : {expense.category}")
        def total_expenses(self):
            total = sum(expense.amount for expense in self.expenses )
            print(f"Total Expenses : ${total:.2f}")
        def Plot_expense_by_category(self):
            category = [expense.category for expense in self.expenses]
            amount = [expense.amount for expense in self.expenses ]

            #Total amount by category
            category_totals = {}
            for category, amount in zip(category, amount):
                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount
            plt.figure(figsize=(8, 6))
            plt.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%', startangle=140)
            plt.title("Expenses by Category")
            plt.show()

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expense")
        print("4. View Plot by category")
        print("5. Total Expenses")
        print("6. Exit")

        choice = input("Enter your Choice (1-5): ")

        if choice =="1":
            date = input(" Enter date ( DD/MM/YYYY): ")
            description = input("Enter the purpose for your expense: ")
            category = input(" Select one Want/Need: ")
            amount = float(input("Enter the amount : $"))
            expense = Expense( date, description, amount, category)
            tracker.add_expense(expense)
            print("Expense added successfully ")
        elif choice == "2":
            index = int(input("Enter the index of the expense to remove : ")) - 1
            tracker.remove_expense(index)
        elif choice =="3":
            tracker.view_expenses()
        elif choice =="4":
            tracker.Plot_expense_by_category()
        elif choice == "5":
            tracker.total_expenses()
        elif choice =="6":
            print("Good Bye!")
        else:
            print("INVALID CHOICE, PLEASE PICK RIGHT ONE")
if __name__ == "__main__":
    main()