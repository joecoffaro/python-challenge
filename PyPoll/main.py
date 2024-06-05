import os
import csv

# set path

file_path = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
print(file_path)

# variables

total_votes = 0
candidate_info = {}
candidate = []
winning_candidate = ""
winning_count = 0


# Open and read csv

with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
    for row in csvreader:
        # total number of votes
        total_votes = total_votes + 1
       
        candidate_name = row[2]
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            candidate_info[candidate_name] = 0
        candidate_info[candidate_name] = candidate_info[candidate_name] +1
        
        # candiate name and votes

file_path = os.path.join(os.path.dirname(__file__), "analysis", "analysis.txt")




with open(file_path, "w") as output_file:

    output = (
     f"Election Analysis\n"
     f"-------------------------\n"
     f"Total Votes: {total_votes}\n"
     f"--------------------------\n"
    )
    print(output)
    output_file.write(output)
    for candidate in candidate_info:
        votes = candidate_info.get(candidate)
        
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # percent of votes 
        if (votes > winning_count):
             winning_count = votes
             winning_candidate = candidate  

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes}) \n"
        print(voter_output)

        output_file.write(voter_output)

    winning_candidate_summary = (
         f"----------------------\n"
         f"Winner: {winning_candidate}\n"
         f"--------------------------\n"
    )
    print(winning_candidate_summary)

    output_file.write(winning_candidate_summary)
    
    
 

# print("Results")   
# print("-------------------------")
# print("Total Votes: " + str(total_votes))    
# print("-------------------------")
# for i in range(len(candidate_info)):
#             print(candidate_info[i] + ": " + str(percent[i]) +"% (" + str(votes[i])+ ")")
# print("-------------------------")
# print("winner: " + winner)


# Print to analysis file

# with open('C:\\Users\\Joe Coffaro\\Desktop\\python-challenge\\PyPoll\\analysis\\analysis.txt', 'w') as text:
#     text.write("Results\n")
#     text.write("---------------------------------------\n")
#     text.write("Total Vote: " + str(total_votes) + "\n")
#     text.write("---------------------------------------\n")
#     for i in range(len(set(candidate_info))):
#         text.write(candidate_info[i] + ": " + str(percent[i]) +"% (" + str(votes[i]) + ")\n")
#     text.write("---------------------------------------\n")
#     text.write("winner: " + winner + "\n")
    


