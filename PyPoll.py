# The data we need to retrieve.
import csv 
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. The total number of votes cast
# 1a. Initialize a total vote counter.
total_votes = 0
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    for row in file_reader:
        # 1b. Add to the total vote count.
        total_votes += 1

# 2. A complete list of candidates who received votes
        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

# Print the candidate list.
print(f"The total number of votes cast is {total_votes}.")
print(f"The names of the candidates voted for are {candidate_options}.")

# 3. The percentage of votes each candidate won
# 4. The total number of  votes each candidate won
# 5. The winner of the eletion based on popular vote