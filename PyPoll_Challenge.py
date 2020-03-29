
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

#Candidate options and votes
candidate_options= []
candidate_votes={}

#County list and votes
county_list =[]
county_votes = {}


#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#County with the largest turnout
county_largestTurnout = ""
largest_turnout = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze the data here. 
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
    

        #Add a vote to that condidate's count (***Must be outside of the if statement but inside the for loop)
        candidate_votes[candidate_name] += 1


        #Print county names from each row
        county_names = row[1]

        #If county doesn't match any existing county
        if county_names not in county_list:

            #Add county names to county list
            county_list.append(county_names)

            #Begin tracking that county's turnout
            county_votes[county_names]=0

        #Add a vote to that county's count
        county_votes[county_names] += 1
       
    #print(county_list)
    #print(county_votes)


#Save results to txt file
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")


    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Add a title for county turnout results
    county_turnout_title= ("\nCounty Votes: \n")
    print(county_turnout_title)
    txt_file.write(county_turnout_title)

    #Iterate thru the county list
    for county in county_list:
        county_turnout = county_votes[county]
        turnout_rate= float(county_turnout/float(total_votes)) * 100
        county_turnoutResults = (
            f"{county}: {turnout_rate: .1f}% ({county_turnout:,})\n")
        
        print(county_turnoutResults)
        txt_file.write(county_turnoutResults)

    #Determine county with largest turnout 
    county_largestTurnout = max(county_votes, key=county_votes.get)
    
    county_turnout_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {county_largestTurnout}\n"
        f"-------------------------\n")
    
    #Print county turnout summary
    print(county_turnout_summary)
    txt_file.write(county_turnout_summary)
    

    #Iterate thru the candidate list
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        #Calculate the percentage of vote each candidate got
        vote_percentage = float(votes)/ float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")  
        
        print(candidate_results)
        txt_file.write(candidate_results)
                
        # Determine winning vote count, winning percentage, and candidate.
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
    
    #Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    
        
    

