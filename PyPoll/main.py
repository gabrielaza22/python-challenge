import csv

# Set path for file
csvpath =  "python-challenge/PyPoll/Resources/election_data.csv"



#variables
total_votes= 0

list_candidates={}
percentage=0
value_votes=0
calculate_percentage=0 

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #  Skip Header
    csv_header= next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
    
            # The total number of votes cast
        total_votes= total_votes + 1
    
        # variable
        candidates_info= row[2]

        # A complete list of candidates who received votes
        if candidates_info in list_candidates.keys():
                list_candidates[candidates_info] += 1
        
        else:
                list_candidates[candidates_info] = 1


    # winner results

    winner=""
    winner_votes=0


    
    # Print election results
    
    winner = max(list_candidates, key=list_candidates.get)

    


    # get the percentage per candidate
    # I tried to use the .values function to create a dictionary with just the
    #values per candidate but would figured to make the loop work
    #Ask the Xpert

    for candidate, votes in list_candidates.items():
        percentage = (value_votes / total_votes) * 100
        value_votes= list_candidates[candidate]
      

    print("Election Results")
    print("Total Votes", total_votes)
    print(f"{candidate}: {percentage:.3f}% ({value_votes})\n")
    print(f"Winner: {winner}n")



    output_file = "election_results.txt"

with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("------------------\n")
    file.write(f"{candidate}: {percentage:.3f}% ({value_votes})\n")
    file.write("------------------\n")
    file.write((f"Winner: {winner}n"))
  

print("Analysis results have been exported to", output_file)
      


    
    
   
