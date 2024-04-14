import pandas as pd

# Read the dataset
df = pd.read_csv("C:/Users/rekha/Downloads/Starter_Code (7)/Starter_Code/PyBank/Resources/budget_data.csv")

# Display the total number of months
total_months = len(df)
print("Total number of months:", total_months)

# Calculate the net total amount of "Profit/Losses"
net_profit_losses = df["Profit/Losses"].sum()
print("Net total amount of Profit/Losses:", net_profit_losses)

# Calculate the changes in Profit/Losses over the entire period
df["Change"] = df["Profit/Losses"].diff()

# Calculate the average of those changes
average_change = df["Change"].mean()
print("Average of changes in Profit/Losses:", average_change)

# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase = df[df["Change"] == df["Change"].max()]
greatest_increase_date = greatest_increase["Date"].values[0]
greatest_increase_amount = greatest_increase["Change"].values[0]
print("Greatest increase in profits:")
print("Date:", greatest_increase_date)
print("Amount:", greatest_increase_amount)

# Find the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = df[df["Change"] == df["Change"].min()]
greatest_decrease_date = greatest_decrease["Date"].values[0]
greatest_decrease_amount = greatest_decrease["Change"].values[0]
print("Greatest decrease in profits:")
print("Date:", greatest_decrease_date)
print("Amount:", greatest_decrease_amount)

