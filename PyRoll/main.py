# first we will Import modules
import os
from datetime import datetime
import csv

# Import, Process, and cleanse csv file
def process_data(file_path):
    total_vote = 0
    candidates = {}
    csv_path = os.path.join(file_path)

    with open(csv_path, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        csv_header = next(csv_reader)
        for row in csv_reader:
            total_vote += 1
            candidate_name = row[2]
            if candidate_name not in candidates:
                candidates.update({candidate_name : 1})
            else:
                candidates[candidate_name] = candidates[candidate_name] + 1 
    return candidates, total_vote

# Output result with expected insights
def create_result(candidates, total_vote):
    
    highest_percentage = 0
    winner_name = ""
    result = ""

    result += "Election Results \n"
    result += "------------------------------ \n"
    result += f"Total Votes: {total_vote} \n"    
    result += "------------------------------ \n"

    # iterate through dictionary
    for candidate in candidates:
        candidate_votes = candidates[candidate]
        percentage = round((candidate_votes / total_vote) * 100, 3)
        if percentage > highest_percentage:
            highest_percentage = percentage
            winner_name = candidate
        result += f"{candidate}: {percentage}%  ({str(candidate_votes)}) \n"

    result += "------------------------------- \n"
    result += f"Winner : {winner_name} \n"
    result += "-------------------------------"
    return result

# write result to console and a text file
def write_results(result):
    print(result)
    with open("{:%B %d, %Y}".format(datetime.now()) + ".txt", "w") as file:
        file.write(result)
    
# Main function to decide the flow and usage of other functions
def main():
    file_path = f"Resources\\election_data.csv"
    candidates, total_vote = process_data(file_path)
    result = create_result(candidates, total_vote)
    write_results(result)

# execute main function
main()