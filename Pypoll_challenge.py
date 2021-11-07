# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

path = 'C:/Users/ryanj/Berkeley_Data_Analysis/week5'

# Add a variable to load a file from a path.
file_to_load = os.path.join(path, "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join(path, "election_results.txt")

#standard spacer for print formating
spacer = '-------------------------\n'

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
c_winning_percentage = 0

# 1: Create a county list and county votes dictionary.
county = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
total_county_votes = 0
largest_county = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county:   

            # 4b: Add the existing county to the list of counties.
            county.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f'{spacer}'
        f"Total Votes: {total_votes:,}\n"
        f'{spacer}'
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes.keys():

        # 6b: Retrieve the county vote count.
        c_votes = county_votes.get(county)

        # 6c: Calculate the percentage of votes for the county.
        c_vote_percentage = float(c_votes) / float(total_votes) * 100

        # 6d: Print the county results to the terminal.
        county_results = (
            f"{county}: {c_vote_percentage:.1f}% ({c_votes:,})\n")

        # 6e: Save the county votes to a text file.
        county_result = (f'{county}: {c_vote_percentage:.1f}% ({c_votes:,})')


        print(county_results, end='')
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if c_votes > largest_county:
            largest_county = c_votes

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_name = (list(county_votes.keys())[list(county_votes.values()).index(largest_county)])

    county_print = (
        f'\n'
        f'{spacer}'
        f'Largest County Turnout: {largest_county_name}\n'
        f'{spacer}'
        f'\n'          
        )
    print(county_print, end='')

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_print)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f'{spacer}'
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f'{spacer}')
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
