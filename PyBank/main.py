import os

import csv

print(dir(csv))

print(os.getcwd())


budgetcsv = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")

with open(budgetcsv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")

    # Print the tota number of months included in the dataset

    for row in cvsreader:
        print("Total Months: ",len(row))
#     list= (row[0])
#     def Number_of_Months(row[0]):
#         count=0
#         for months in row[0]:
#             count+= 1
#         return count
# print("Total Months: ", Number_of_Months(row[0]))


    #The net total amount of 'Profit/Losses' over the entire perioed, and then the average of those changes


    #The greatest increase in profits (date and amount) over the entire period


    #The greatest decrease in profits (date and amount) over the entire period

  



    
