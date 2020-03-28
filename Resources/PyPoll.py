#The data we need to retrive.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
# Add our dependencies.


import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

#Candidate options
candidate_options= []

#Candidate votes
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    file_reader=csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
 

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        
        #Print candidate names from each row
        candidate_name = row[2]
        
        #If the candidate doesn't match any existing candidate
        if candidate_name not in candidate_options:

            #Add candidate names to candidate_options
            candidate_options.append(candidate_name)
            
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        
        #Add a vote to that condidate's count (Must be outside of the if statment)
        candidate_votes[candidate_name] += 1
    
    #Iterate thru the candidate list
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        #Calculate the percentage of vote each candidate got
        vote_percentage = float(votes)/ float(total_votes) * 100
    
        print(f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
        
        if (votes) > (winning_count) and (vote_percentage) > (winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    
    

