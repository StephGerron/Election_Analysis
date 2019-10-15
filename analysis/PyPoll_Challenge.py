#Add our dependancies.
import csv
import os

# Create a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#Candidate options
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}

#County options
county_options = []
#Declare the empty dictionary
county_votes = {}

# Largest county votes and count tracker
largest_county = ""
largest_count = 0
largest_percentage = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Hyphen 
hyphen_variable = "-"

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)

    #print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2] 
        # Print the county name from each row.
        county_name = row[1]

        # If the county does not match any existing county
        if county_name not in county_options:
            # Add county name to the county list.
            county_options.append(county_name)
            # 2. Begin tracking that county's vote count.
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1 


        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add candidate names to the candidate list.
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:    
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"{hyphen_variable*25} \n"
        f"Total Votes: {total_votes:,} \n"
        f"{hyphen_variable*25} \n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    county_results = (
        f"\nCounty Votes:\n")
    print(county_results, end="")
    #write txt
    txt_file.write(county_results)

    for county in county_votes:
        # 2. Retrieve vote count of a candidate.
        county_tally = county_votes[county]
        # 3. Calculate the percentage of votes.
        county_percentage = float(county_tally) / float(total_votes) * 100
        county_results = (f"{county}: {county_percentage:.1f}% ({county_tally:,})\n")
        #print
        print(county_results, end="")
        #write txt
        txt_file.write(county_results)

        # Determine total votes per county
        # 1. Determine if the votes are greater than 
        if (county_tally > largest_count) and (county_percentage > largest_percentage):
            # 2. If true then set  = votes and  =
            # vote_percentage.
            largest_county = county
            largest_count = county_tally
            largest_percentage = county_percentage
        
    # Print the county vote totals to the terminal
    county_results = (
        f"\n{hyphen_variable*25} \n"
        f"Largest County Turnout: {largest_county}\n"
        f"{hyphen_variable*25} \n")
    print(county_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(county_results) 

    # Determine the percentage of votes for each candidate and county by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results, end="")
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"{hyphen_variable*25} \n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"{hyphen_variable*25} \n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

    