
#import csv and os modules
import os
import csv

month = []
profit = []
monthlychanges = []

#open CSV and read it, update lists for months and total profits 

budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')
budget = open(budget_csv, "r")
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        profit.append(float(row[1]))
        month.append(str(row[0]))
    for i in range(1, len(month)):
        changes = (profit[i]-profit[i-1])
        monthlychanges.append(changes)
    
    #determin best and worse months of profit
    greatprofit = max(monthlychanges)
    worstloss = min(monthlychanges)
    pgreatprofit = monthlychanges.index(greatprofit)
    pworstprofit = monthlychanges.index(worstloss)
    #find the month in which best and worse profits occured
    #have to shift month by 1 as the monthly changes starts 1 element later (if in excel, it would start at row 2 instead of 1)
    greatmonth = month[pgreatprofit+1]
    worstmonth = month[pworstprofit+1]

    
#find the totalprofit and number of months at which the financial statement is from:
totalprofit = sum(profit)
totalmonths = len(month)
averagechanges = sum(monthlychanges)/(totalmonths-1)

#print out the results into the terminal
print("Financial analysis:")
print(" ")
print("---------------------------------------------")
print(" ")
print(f'Total Months: {totalmonths}')
print(" ")
print(f'Total: ${totalprofit}')
print(" ")
print(f'Average Change: ${round(averagechanges, 2)}')
print(" ")
print(f'Greatest Increase in Profit: {greatmonth} (${greatprofit})')
print(" ")
print(f'Greatest Decrease in Profit: {worstmonth} (${worstloss})')
print(" ")

#print out the results into a txt file
write = ["Financial analysis:",
" ",
"---------------------------------------------",
" ",
f'Total Months: {totalmonths}',
" ",
f'Total: ${totalprofit}',
" ",
f'Average Change: ${round(averagechanges, 2)}',
" ",
f'Greatest Increase in Profit: {greatmonth} (${greatprofit})',
" ",
f'Greatest Decrease in Profit: {worstmonth} (${worstloss})',
" "]

with open("mainbank.txt", "w") as text:
    for info in write:
        text.write(info)
        text.write("\n")






