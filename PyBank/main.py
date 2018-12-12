import pandas as pd
import os

#reading csv and assigning to a dataframe
bankcsv = os.path.join("..", "budget_data.csv" )
bankData_df = pd.read_csv(bankcsv)

#finding total months and revenue
months = len(bankData_df["Date"])
totRevenue = sum(bankData_df["Profit/Losses"])

#finding the difference between profit/loss values
bankData_df["Diff Revenue"] = bankData_df["Profit/Losses"].diff()

#finding the record with the maximum increase and minimum increase
maxRecord = bankData_df.loc[bankData_df["Diff Revenue"] == bankData_df["Diff Revenue"].max()]
minRecord = bankData_df.loc[bankData_df["Diff Revenue"] == bankData_df["Diff Revenue"].min()]

print("Financial Analysis")
print("----------------------------")
print(f'Number of months is {months}')
print(f'Total revenue is {totRevenue}')
print(f'Average  Change: ${round(bankData_df.loc[:,"Diff Revenue"].mean(),2)}')
print(f'Greatest Increase in Profits : {maxRecord.iloc[0,0]} ${bankData_df["Diff Revenue"].max()}')
print(f'Greatest Decrease in Profits : {minRecord.iloc[0,0]} ${bankData_df["Diff Revenue"].min()}')

f = open('Revenue_Analysis.txt','w')
f.write("Financial Analysis \n")
f.write("----------------------------\n")
f.write(f'Number of months is {months} \n')
f.write(f'Total revenue is {totRevenue} \n')
f.write(f'Average  Change: ${round(bankData_df.loc[:,"Diff Revenue"].mean(),2)} \n')
f.write(f'Greatest Increase in Profits : {maxRecord.iloc[0,0]} ${bankData_df["Diff Revenue"].max()} \n')
f.write(f'Greatest Decrease in Profits : {minRecord.iloc[0,0]} ${bankData_df["Diff Revenue"].min()} \n')
f.close()
