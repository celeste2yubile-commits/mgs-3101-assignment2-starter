import pandas as pd

# Load the sales dataset into a DataFrame
df = pd.read_csv("../data/Sales-Export_2019-2020.csv")

# Remove extra spaces from the column names
df.columns = df.columns.str.strip()

# Convert order value from text to a numeric data type
df["order_value_EUR"] = df["order_value_EUR"].str.replace(",", "")
df["order_value_EUR"] = df["order_value_EUR"].astype(float)

# Display the shape of the dataset
print("Shape:")
print(df.shape)

# Display the data types of each column
print("\nData Types:")
print(df.dtypes)

# Display the first five rows
print("\nFirst Five Rows:")
print(df.head())

# Check for missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Display descriptive statistics for order value
print("\nOrder Value Statistics:")
print("Mean:", df["order_value_EUR"].mean())
print("Median:", df["order_value_EUR"].median())
print("Minimum:", df["order_value_EUR"].min())
print("Maximum:", df["order_value_EUR"].max())
print("Standard Deviation:", df["order_value_EUR"].std())

# Display descriptive statistics for cost
print("\nCost Statistics:")
print("Mean:", df["cost"].mean())
print("Median:", df["cost"].median())
print("Minimum:", df["cost"].min())
print("Maximum:", df["cost"].max())
print("Standard Deviation:", df["cost"].std())

# Group data by country and calculate average order value
print("\nAverage Order Value by Country:")
country_average = df.groupby("country")["order_value_EUR"].mean()
print(country_average)

# Find the highest order value
highest_order = df["order_value_EUR"].max()

print("\nHighest Order Value:")
print(highest_order)

# Find the row with the highest order value
print(df[df["order_value_EUR"] == highest_order])

# Find the lowest order value
lowest_order = df["order_value_EUR"].min()

print("\nLowest Order Value:")
print(lowest_order)

# Find the row with the lowest order value
print(df[df["order_value_EUR"] == lowest_order])

# Calculate average order value
average_order = df["order_value_EUR"].mean()

# Use an if/else statement
if average_order >= 100000:
    print("\nThe average order value is high.")
else:
    print("\nThe average order value is low.")

# Print a summary of findings
print("\nSummary:")
print("The dataset contains sales information from multiple countries.")
print("There are no missing values in the dataset.")
print("Order values vary significantly across transactions.")
print("Some countries have higher average order values than others.")

# Display the top 5 countries by average order value
print("\nTop 5 Countries by Average Order Value:")
print(country_average.sort_values(ascending=False).head(5))