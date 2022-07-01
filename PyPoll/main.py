'''
PyPoll

In this Challenge, I was tasked with helping a small, rural town modernize its vote-counting process.
I was given a set of poll data called election_data.csv composed of three columns: "Voter ID", "County", and "Candidate". 

I was asked to analyze the votes to calculate:
    The total number of votes cast
    A complete list of candidates who received votes
    The percentage of votes each candidate won
    The total number of votes each candidate won
    The winner of the election based on popular vote
'''
# module imports
import os
import csv
import sys

# variables 
total_votes = 0
winner_votes = 0
candidates = {}

# initialaizations
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') # CSV reader 
    print(csvreader)

    csv_header = next(csvreader) # skip header row
    print(f"CSV Header: {csv_header}\n")

    # main loop
    for row in csvreader:
        total_votes = total_votes + 1

        if row[2] in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1

        if candidates[row[2]] > winner_votes:
            winner = row[2]
            winner_votes = candidates[row[2]]

# define text file
txtpath = os.path.join('Analysis', 'Analysis.txt')
stdout_init = sys.stdout 

# redirect output to file
with open(txtpath, "w") as txtfile:
    sys.stdout = txtfile

    # print results to file
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")       
    print("----------------------------")

    for key, value in candidates.items():
        print(f"{key}: {100 * (int(value))/total_votes:.3f}% ({int(value)})") 

    print("----------------------------")
    print(f"Winner: {winner}")     
    print("----------------------------")

# reset output to normal
sys.stdout = stdout_init 

# print to terminal
with open(txtpath, "r") as txtfile:
    txtfilecontent = txtfile.read()
    print(txtfilecontent)
