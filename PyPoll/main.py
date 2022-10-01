#Libraries
import os

import csv

print(os.getcwd())


#Input File

#Output File

votingpath = os.path.join("Resources", "election_data.csv")
outpath = os.path.join("analysis", "poll_results.txt")

#Variables

total_votes= 0
list_of_votes= []

candidates = []

list_of_names= []

vote_percent= []





with open (votingpath) as csv_file:
   
    csv_reader= csv.reader(csv_file, delimiter = ",")

    csv_header= next(csv_reader)

    csv_first= next(csv_reader)

    total_votes = total_votes +1




    for row in csv_reader:

        total_votes+= 1
        

        #if statement to uncover complete list of candidates who received votes 
        if row[2] not in candidates:
            candidates.append(row[2])

        list_of_votes.append(row[2])

#Use a forloop to see the complete list of candidates wo=ho received votes
#     for row in list_of_names:
#         candidates.append(list_of_votes.count(row))

#         vote_percent.append(round(list_of_votes.count(row)/total_votes*100))

# #find the winner of the election
# winner= list_of_names[candidates.index(max(candidates))]


    












#format output
output= (
    f"Election Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------\n"





)

print(output)

# with open(outpath,"w") as text_file: 
#     text_file.write(output)