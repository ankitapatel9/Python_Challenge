# import modules
import os
import csv
import numpy as np
# Import, Process, and cleanse csv file
csv_path = os.path.join("Resources", "budget_data.csv")
total_months = 0
total_amount = 0

greatest_profit = 0
greatest_profit_month = ""

greatest_loss = 0
greatest_loss_month = ""

change_in_profit = []
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    previous_amount = 0
    is_first_row = True

    for row in csv_reader:
        current_month = row[0]
        current_amount = float(row[1]) 

        total_months += 1
        total_amount += current_amount        
        
        current_profit = current_amount - previous_amount

        if current_profit > greatest_profit:
            greatest_profit = current_profit
            greatest_profit_month = current_month
        if current_profit < greatest_loss:
            greatest_loss = current_profit   
            greatest_loss_month = current_month
        
        # finding avarage change of value

        previous_amount = current_amount

        if is_first_row:
            is_first_row = False
            continue
        change_in_profit.append(current_profit)


    average_change = round((sum(change_in_profit))/ max(len(change_in_profit), 1),2)
    # string concatanation
    result = ""
    result += "Financial Analysis\n"
    result += "------------------------\n"
    result += f"Total Months: {total_months}\n"
    result += f"Total: {total_amount}\n"
    result += f"Average  Change: ${average_change}\n"
    result += f"Greatest Increase in Profits: {greatest_profit_month} $({greatest_profit})\n"
    result += f"Greatest Decrease in Profits: {greatest_loss_month} $({greatest_loss})\n"
    result += "------------------------\n"
    print(result)
    # wiring text file
    with open("PyBank.txt", "w") as file:
        file.write(result)