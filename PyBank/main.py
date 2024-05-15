
import csv

# Set path for file
csvpath =  "python-challenge/PyBank/Resources/budget_data.csv"

#Variables
month_count= 0
net_total= 0
last_month=()
average_change=0
greatest_increase=0
greatest_month=0
month_changes=[]
greatest_decrease=0
decrease_month=0

#Create the list for the changes
changes = []


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #  Skip Header
    csv_header= next(csvreader)
    print(f"CSV Header: {csv_header}")

    

    # Actual rows after the header
    for row in csvreader:
        
   
       # Count months/ Each row is a month
        month_count= month_count + 1

   
        # profit and total losses
        net_total = net_total + int(row[1])
    	
        # difference last month to actual month
        
        if (month_count==1):
            last_month = int(row[1])
        else:
            difference = int(row[1])- last_month
            changes.append(difference)
            month_changes.append(row[0])

        # go back to the first row.Reset
           
            last_month = int(row[1])
    average_change= sum(changes) / len(changes)
           
    greatest_increase= max(changes)
    # we use the results from the max along with the index to get the month
    greatest_month_num= changes.index(greatest_increase)
    greatest_month= month_changes[greatest_month_num]
   
    # greatest decrease. we repeat the process but using the min
    greatest_decrease= min(changes)
    decrease_month_num= changes.index(greatest_decrease)
    decrease_month= month_changes[decrease_month_num]
   
    print ("Financial Analysis")
    print("Total Months: ", month_count)
    print("Total ", net_total)
    print("differences ", len(changes))
    print("Average change $", average_change)
    print("Greatest Increase in Profits: ", greatest_month, greatest_increase)
    print("Greatest Decrease in Profits: ", decrease_month, greatest_decrease )

output_file = "financial_analysis_budget.txt"

with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {net_total}\n")
    file.write(f"Total: ${len(changes)}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")

print("Analysis results have been exported to", output_file)