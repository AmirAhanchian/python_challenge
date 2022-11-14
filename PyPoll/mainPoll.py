#import csv and OS modules
import os
import csv

ballots = []
candidate = []
uniquecandidates = []

print("Election Results:")
print(" ")
print("---------------------------------------------")
print(" ")


#open CSV and read it, update lists for candidates and the ballots

election_csv = os.path.join('.', 'Resources', 'election_data.csv')
#print(election_csv)
budget = open(election_csv, "r")
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        candidate.append(str(row[2]))
        ballots.append(str(row[0]))
    #print(len(ballots))
    #print(len(candidate))
    
    
#find list of candidates
uniquecandidates = []
for name in candidate:
    if name not in uniquecandidates:
         uniquecandidates.append(name)
#print(uniquecandidates)

#find vote count for each candidate
Stockham_votes = candidate.count(uniquecandidates[0])
#print(Stockham_votes)
DeGette_votes = candidate.count(uniquecandidates[1])
Doane_votes = candidate.count(uniquecandidates[2])

#find percentage of votes per candidate
percent_Stockham = round((Stockham_votes/(len(ballots)))*100,3)
#print(percent_Stockham)
percent_DeGette = round((DeGette_votes/(len(ballots)))*100,3)
percent_Doane = round((Doane_votes/(len(ballots)))*100,3)

#declair the winner
popular_vote = [Stockham_votes, DeGette_votes, Doane_votes]
who_won_position = popular_vote.index(max(popular_vote))
who_won = uniquecandidates[who_won_position]
#print(who_won)

#print the results of the election into terminal
print("Election Results:")
print(" ")
print("---------------------------------------------")
print(" ")
print(f'Total Votes: {len(ballots)}')
print(" ")
print("---------------------------------------------")
print(" ")
print(f'{uniquecandidates[0]}: {percent_Stockham}% ({Stockham_votes})')
print(" ")
print(f'{uniquecandidates[1]}: {percent_DeGette}% ({DeGette_votes})')
print(" ")
print(f'{uniquecandidates[2]}: {percent_Doane}% ({Doane_votes})')
print(" ")
print("---------------------------------------------")
print(" ")
print(f'Winner: {who_won}')
print(" ")
print("---------------------------------------------")


#print out the results into a txt file
write = ["Election Results:",
" ",
"---------------------------------------------",
" ",
f'Total Votes: {len(ballots)}',
" ",
"---------------------------------------------",
" ",
f'{uniquecandidates[0]}: {percent_Stockham}% ({Stockham_votes})',
" ",
f'{uniquecandidates[1]}: {percent_DeGette}% ({DeGette_votes})',
" ",
f'{uniquecandidates[2]}: {percent_Doane}% ({Doane_votes})',
" ",
"---------------------------------------------",
" ",
f'Winner: {who_won}',
" ",
"---------------------------------------------"]

mainpoll = os.path.join('.', 'Analysis', 'mainPoll.txt')

with open(mainpoll, "w") as text:
    for info in write:
        text.write(info)
        text.write("\n")