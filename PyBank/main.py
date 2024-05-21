import csv



file = './Resources/budget_data.csv'

first_row = True
month = 0
profit_loss = 0
first_row = True
previous_profit_losses = 0
changes = []
total_profit_losses = 0

with open(file, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader) ## remove header

    profit_losses_index = csv_header.index("Profit/Losses")
    
## calculate total months and total profit/losses

    for row in csvreader:
        month = month +1 
        
        profit_loss += int(row[profit_losses_index])


        current_profit_losses = int(row[1])

        if not first_row:
            change = current_profit_losses - previous_profit_losses
            changes.append(change)
        else:
            first_row = False  # After the first iteration, this becomes False
            
            # Update the previous value to the current one

        previous_profit_losses = current_profit_losses

## average change 
        
    if changes:
        average_change = sum(changes) / len(changes)
    else:
        average_change = 0

    average_change = round(average_change, 2)

##------------- greatest change and lowest change with month

    highest_change = max(changes)
    highest_change_index = changes.index(highest_change)

    highest_change_index = changes.index(highest_change) + 1  # Adjust index by adding 1

    # Reset csvreader
    csvfile.seek(0)
    next(csvreader)  # Skip header
    for _ in range(highest_change_index):  # Skip rows until reaching the highest change row
        next(csvreader)
    highest_change_month = next(csvreader)[0]

   
    
    lowest_change = min(changes)
    lowest_change_index = changes.index(lowest_change)

    lowest_change_index = changes.index(lowest_change) + 1  # Adjust index by adding 1

    # Reset csvreader
    csvfile.seek(0)
    next(csvreader)  
    for _ in range(lowest_change_index):  # Skip rows until reaching the highest change row
        next(csvreader)
    lowest_change_month = next(csvreader)[0]  
    

# output = (
#     (f"Month: {month} \nSum of Profit/Losses: {profit_loss}"),
#     (f"Average Change in Profit/Losses: {average_change}"),
#     (f"Highest Change in Profit/Losses: ${highest_change} (Month: {highest_change_month})"),
#     (f"Lowest Change in Profit/Losses: ${lowest_change} (Month: {lowest_change_month})")
# )

output = (
    f"FinancialAnalysis\n"
    f"-------------------------\n"
    f"Month: {month} \nSum of Profit/Losses: {profit_loss}\n"
    f"Average Change in Profit/Losses: {average_change}\n"
    f"Highest Change in Profit/Losses: ${highest_change} (Month: {highest_change_month})\n"
    f"Lowest Change in Profit/Losses: ${lowest_change} (Month: {lowest_change_month})\n"
)
print(output)
output_file = ('./analysis/analysis.txt')
with open(output_file, 'w') as file:
    file.write(output)