
import pandas as pd

# Read the dataset
df = pd.read_csv("C:/Users/rekha/Downloads/Starter_Code (7)/Starter_Code/PyPoll/Resources/election_data.csv")

# Calculate the total number of votes cast
total_votes = df["Ballot ID"].count()
print("Total number of votes cast:", total_votes)

# Get a list of unique candidates who received votes
candidates = df["Candidate"].unique()

# Initialize a dictionary to store the total number of votes for each candidate
candidate_votes = {}

# Iterate through each candidate and count their votes
for candidate in candidates:
    candidate_votes[candidate] = df[df["Candidate"] == candidate]["Ballot ID"].count()

# Print the complete list of candidates who received votes and the total number of votes each candidate won
print("Complete list of candidates who received votes and their total number of votes:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes")

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Print the percentage of votes each candidate won
print("\nPercentage of votes each candidate won:")
for candidate, percentage in candidate_percentages.items():
    print(f"{candidate}: {percentage:.2f}%")

# Determine the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
print("\nWinner of the election based on popular vote:", winner)

