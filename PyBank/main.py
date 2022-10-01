#Libraries 
import os

import csv

print(os.getcwd())

#Input File

#Output File

budgetpath = os.path.join("Resources", "budget_data.csv")
outpath = os.path.join("analysis", "results.txt")
#Variables

total_months = 0
total_net= 0




with open(budgetpath) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header = next(csv_reader)

    csv_first = next (csv_reader)
    
    total_months = total_months + 1
    #one line of code for the total net and one line for the previous net 
    total_net += int(csv_first[1])
    previous_net= int(csv_first[1])

    for row in csv_reader:

        total_months+=1
        total_net += int(row[1])


        #net change

        previous_net = (int(row[1])-previous_net)/

        #if statement to caluclate the greatest increase


        #if statement to calculate the greatest decrease



#net monthly average 










#format output
output= (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${previous_net}\n"




)

print(output)

with open(outpath,"w") as text_file: 
    text_file.write(output)
       
#


    #The net total amount of 'Profit/Losses' over the entire perioed, and then the average of those changes


    #The greatest increase in profits (date and amount) over the entire period


    #The greatest decrease in profits (date and amount) over the entire period

  



    
