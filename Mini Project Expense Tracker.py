expenses = []
categories = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Others"]
# user_category_count = int(input("Enter How many categories you want in integer"))
# categories = []
# for i in range(1,user_category_count+1):
#   val = input("Enter a Category Name").lower().strip()
#   categories.append(val)


while True:
  print("="*40)
  print("PERSONAL EXPENSE TRACKER".center(40))
  print("="*40)
  print("1. Add New Expense")
  print("2. View All Expenses")
  print("3. Category Summary")
  print("4. Set/Check Budget")
  print("5. Search Expenses")
  print("6. Exit")
  print("="*40)
  choice = (input("Enter your choice (1-6): "))
  if (choice == "1"):
    print("--- ADD NEW EXPENSE ---")
    print(f'Available categories: {",".join(categories)}')
    #lower and strip is something you guys have to do for every character input
    category = input("Enter category : ")
    if category in categories:
      pass
    else:
      print("category You entered is not available, hence we will put it in Others")
      category = "Others"
    amount = float(input("Enter amount : "))
    desc = input("Enter desc : ")
    expense = {}
    expense["category"] = category
    expense["amount"] = amount
    expense["desc"] = desc

    # expense={"category":category,"amount":amount,"des":description}
    expenses.append(expense)
    print("\n✓ Expense added successfully!")
    #print(expenses)
  elif choice == "2":
    count = 1
    total = 0
    for i in expenses: # i = 'category': 'Food', 'amount': 1000.0, 'desc': 'Macd'}
      print(f"#{count:<5} | {i['category']:<20} | {i['amount']:<10} | {i['desc']:<30} ")
      count = count + 1
      total = total + i['amount']
    print("-"*66)
    print(f"Total Expenses: ₹{total:>49}")
    print(f"Total Count of Categories: {count - 1}")
  elif choice == "3":
    summary_cat = {}
    for i in categories:
        summary_cat[i] = 0
    print("--- CATEGORY SUMMARY ---")
    categories_sum = 0
    for i in expenses:
      item = i["category"].title()
      amount = i["amount"]
      summary_cat[item] = summary_cat[item] + amount
    #summary_cat --> {"Food":2000, "Movies":1000}
    for i,j in summary_cat.items():
      if j != 0:
        print(f"{i} : ₹{j}")
        categories_sum = categories_sum + j
    print("----------------------------------------")
    print(f"Total : ₹{categories_sum}")
  elif choice == "4":
    budget=input("Enter Your Budget :")
    if budget != 0:
      pass
      #budget = float(input(f"You have a budget of {budget} do you want to update with new value "))
    else:
      budget = float(input("Please enter a budget"))
      total_expenses = 0
      for i in expenses:
        total_expenses = total_expenses + i["amount"]
      if budget > total_expenses:
        print(f"You can still spend some money, you have {budget - total_expenses} to spend")
      else:
        print(f"You are Over budget my friend by Ruppes:: {total_expenses - budget }")
  elif choice == "5":

      choice = input("Enter a type by which you want to search (category, desc, amount) ")
      if choice == "category":
        select_cat = input("Enter category of search")
        for i in expenses:
          if i["category"].title() == select_cat.title():
            print(i["category"],i["amount"], i["desc"])
      elif choice == "desc":
        select_cat = input("Enter desc of search")
        for i in expenses:
          if i["desc"].title() == select_cat.title():
            print(i["category"],i["amount"], i["desc"])
      elif choice == "amount":
        select_cat = float(input("Enter amount of search"))
        for i in expenses:
          if i["amount"] == select_cat:
            print(i["category"],i["amount"], i["desc"])
  elif choice == "6":
    print("Thank You For Visiting!! Kal fir Ana !!!!!!!")
    break
  else:
    print("\n   Invalid Option, Please try Again")