"""Array Data Structure - Monthly Expenses"""

# 0
expenses = [2200, 2350, 2600, 2130, 2190]

# 1 How much was spent extra in February
feb_extra_expenses = expenses[1] - expenses[0]
print(f'Spent ${feb_extra_expenses} extra compared to January')

# 2 Total Q1 Expense
total_Q1 = sum(expenses[:3])
print(total_Q1)

# 3 Check if exactly 2000 wasa spent in any month
print(2000 in expenses)

# 4 Add 1980 to expenses for June
expenses.append(1980)
print(expenses)

# 5 Subtract 200 from april
expenses[3] = expenses[3] - 200
print(expenses)
