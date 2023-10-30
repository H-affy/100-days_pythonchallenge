print("Welcome to the tip calculator.")
Bill = float(input("What is the total bill? $"))
Percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
Split_bill = int(input("How many people to split the bill? "))

calc_percentage = (Percentage_tip / 100) + 1
calc_bill = (Bill / Split_bill) * calc_percentage
bill = round(calc_bill, 2)
print(f"Each person should pay ${bill}")
