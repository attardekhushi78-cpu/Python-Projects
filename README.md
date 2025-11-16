Personal Expense Tracker – Python Project

A simple and interactive command-line Expense Tracker written in Python.
This program allows users to add expenses, categorize them, view summaries, set budgets, and search past records.

🚀 Features
✅ 1. Add New Expense

Enter category, amount, and description

Automatically assigns "Others" if the entered category is not available

✅ 2. View All Expenses

Displays all expenses in a clean table-like format

Shows:

Total expenses

Total number of entries

✅ 3. Category Summary

Calculates total spending per category

Shows how much you spent on:

Food

Transport

Entertainment

Shopping

Bills

Others

✅ 4. Set / Check Budget

Enter your monthly budget

Program tells you:

How much money is left

OR if you are over budget

✅ 5. Search Expenses

Search expenses by:

Category

Description

Amount

✅ 6. Exit Program

Clean exit from the system.

📂 Categories Included

Food

Transport

Entertainment

Shopping

Bills

Others

🧾 How It Works

The program stores each expense as a Python dictionary:

{
    "category": "Food",
    "amount": 120,
    "desc": "Lunch at McD"
}


All such dictionaries are stored inside a list called expenses.

▶️ How to Run the Program

Make sure Python is installed.

python expense_tracker.py


(Replace expense_tracker.py with your actual filename)

📌 Future Improvements (Optional)

These can be added later to improve the project:

Save expenses to a file

Load previous expenses on startup

Monthly charts using matplotlib

GUI version using Tkinter / PyQt

🎯 Purpose of the Project

This project helps beginners understand:

Python dictionaries

Lists

Loops

Conditional statements

Menu-driven applications
