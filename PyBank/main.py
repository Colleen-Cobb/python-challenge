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
month= []
profits_losses= []
last_value= 0
changes= 0




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

        #Keep track of the month
        month.append(row[0])

        #Keep track of the changes in profi/losses
        changes = int(row[1])-last_value
        profits_losses.append(changes)
        last_value= int(csv_first[1])



        #net change

        
        

        #caluclate the greatest increase
        greatest_increase= max(profits_losses)

        greatest_inc_value= profits_losses.index(greatest_increase)

        greatest_inc_month= month[greatest_inc_value]


        #calculate the greatest decrease
  
        greatest_decrease= min (profits_losses)

        greatest_dec_value= profits_losses.index(greatest_decrease)

        greatest_dec_month= month[greatest_dec_value]


#net monthly average 

average_change= sum(profits_losses)/len(profits_losses)








#format output
output= (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${str(round(average_change,2))}\n"
    f"Greatest Increase in Profits: {greatest_inc_month} (${str(greatest_increase)})\n"
    f"Greastest Decrease in Profits: {greatest_dec_month} (${str(greatest_decrease)})\n"




)

print(output)

with open(outpath,"w") as text_file: 
    text_file.write(output)
       
#


    #The net total amount of 'Profit/Losses' over the entire perioed, and then the average of those changes


    #The greatest increase in profits (date and amount) over the entire period


    #The greatest decrease in profits (date and amount) over the entire period

  



    
