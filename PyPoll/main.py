import csv
import os

pollcsv = os.path.join("..", "election_data.csv" )

# Read in the CSV file
with open(pollcsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    votes = 0
    kVotes = 0
    cVotes = 0
    lVotes = 0
    oVotes = 0
    others = 0
    
    for row in csvreader:
        votes = votes + 1
        if row[2] == "Khan":
            kVotes = kVotes + 1
        elif row[2] == "Correy":             
            cVotes = cVotes +1
        elif row[2] == "Li":
            lVotes = lVotes +1
        elif row[2] == "O'Tooley":
            oVotes == oVotes + 1
        else:
            others == others +1
    
    kPerc = round((kVotes/votes)*100,3)
    cPerc = round((cVotes/votes)*100,3)
    lPerc = round((lVotes/votes)*100,3)
    oPerc = round((oVotes/votes)*100,3)
    
    canDict = {"Khan": kVotes, "Correy":cVotes, "Li":lVotes, "O'Tooley":oVotes}
    #getting the value that has the most votes and find the key
    winner = max(zip(canDict.values(), canDict.keys()))[1]
    
    
print("Election Results") 
print("-------------------------")
print(f'Total Votes: {votes}')
print("-------------------------")
print(f'Khan: {kPerc}% ({kVotes})')
print(f'Correy: {cPerc}% ({cVotes})')
print(f'Li: {lPerc}% ({lVotes})')
print(f"O'Tooley: {oPerc}% ({oVotes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
    
#write the output to a file
f = open('Election_Results.txt','w')
f.write("-------------------------\n")
f.write(f'Total Votes: {votes} \n')
f.write("-------------------------\n")
f.write(f'Khan: {kPerc}% ({kVotes}) \n')
f.write(f'Correy: {cPerc}% ({cVotes}) \n')
f.write(f'Li: {lPerc}% ({lVotes}) \n')
f.write(f"O'Tooley: {oPerc}% ({oVotes}) \n")
f.write("-------------------------\n")
f.write(f"Winner: {winner} \n")
f.write("-------------------------\n")
f.close()
    
        