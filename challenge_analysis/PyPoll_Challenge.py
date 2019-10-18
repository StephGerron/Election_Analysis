#Add our dependancies.
import csv
import os

# Create a variable to load and save a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
file_to_save = os.path.join("challenge_analysis/election_analysis.txt")

# Initialize a total vote counter and then the empty list and dictionary for candidates and counties.
total_votes = 0
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

# Largest county votes and count tracker
largest_county = ""
largest_count = 0
largest_percentage = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Hyphen to standardize formatting.
hyphen_variable = "-"

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)

    #print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Print the candidate and county name from each row.
        candidate_name = row[2] 
        county_name = row[1]

        # If the county does not match any existing county, then add to county list, 3rd begin tracking votes, 4th add to count.
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1 


        # If the candidate does not match any existing candidate, then add to candidate list, 3rd begin tracking votes, 4th add to count.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Open text file and save the results to to the election_analysis text file.
with open(file_to_save, "w") as txt_file:    
    election_results = (
        f"\nElection Results\n"
        f"{hyphen_variable*25} \n"
        f"Total Votes: {total_votes:,} \n"
        f"{hyphen_variable*25} \n")
    print(election_results, end="")
    txt_file.write(election_results)

    county_results = (
        f"\nCounty Votes:\n")
    print(county_results, end="")
    txt_file.write(county_results)

    # Retrieve vote count and calculate percentage of votes for county voter turnout, then print results in text file. 
    for county in county_votes:
        county_tally = county_votes[county]
        county_percentage = float(county_tally) / float(total_votes) * 100
        county_results = (f"{county}: {county_percentage:.1f}% ({county_tally:,})\n")
        
        print(county_results, end="")
        txt_file.write(county_results)

        # Determine total votes per county and largest voter turnout.
        if (county_tally > largest_count) and (county_percentage > largest_percentage):
            largest_county = county
            largest_count = county_tally
            largest_percentage = county_percentage
        
    # Format and print to text file the county turnout results. 
    county_results = (
        f"\n{hyphen_variable*25} \n"
        f"Largest County Turnout: {largest_county}\n"
        f"{hyphen_variable*25} \n")
    
    print(county_results, end="")
    txt_file.write(county_results) 

    # Determine the vote totals and percentages for each candidate, then print candidate, %, and total votes in text file.
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        print(candidate_results, end="")
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Format and print winning candidate with vote count and percentages.
    winning_candidate_summary = (
        f"{hyphen_variable*25} \n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"{hyphen_variable*25} \n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)