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

count_of_votes= []

candidates = []

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
            value_index=candidates.index(row[2])
            count_of_votes.append(1)
        else:
            value_index= candidates.index(row[2])
            count_of_votes[value_index]+= 1
   

    #Use a for loop to find the percentage of votes each candidate won

    for ballot_count in count_of_votes:
        percentage= (ballot_count/total_votes)*100
        percentage= round(percentage,3)
        vote_percent.append(percentage)

    #find the winner of the popular vote
    winner= max(count_of_votes)
    value_index= count_of_votes.index(winner)
    popular_winner=candidates[value_index]


    


#format output
output= (
    f"Election Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------\n"
    f"{candidates[0]}: {str(vote_percent[0])}% ({str(count_of_votes[0])})\n"
    f"{candidates[1]}: {str(vote_percent[1])}% ({str(count_of_votes[1])})\n"
    f"{candidates[2]}: {str(vote_percent[2])}% ({str(count_of_votes[2])})\n"
    f"-----------------------\n"
    f"Winner: {popular_winner}\n"
    f"-----------------------\n"





)

print(output)

with open(outpath,"w") as text_file: 
    text_file.write(output)