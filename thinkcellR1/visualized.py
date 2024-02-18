import pandas as pd

# Create a dictionary with column names and corresponding lists of values
data = {
    "distance": list(
        range(1, 11)
    ),  # Generates a list from 1 to 10 for the 'distance' column
    "sspeed": [5]
    * 10,  # Creates a list of 5s repeated 10 times for the 'sspeed' column
    "bspeed": [10]
    * 10,  # Creates a list of 10s repeated 10 times for the 'bspeed' column
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Calculate the 'time' column based on the formula provided
df["time"] = df["distance"] / df["sspeed"] * df["bspeed"]

# Display the DataFrame
print(df)
