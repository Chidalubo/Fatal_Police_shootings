import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Load the Dataset
# -------------------------------
file_path = "/Users/brayantchidalu/Documents/Data analyst/project 1/shootings.csv"  # Update the path if needed
df = pd.read_csv(file_path)

# Display initial information and a preview of the data
print("Initial Data Info:")
print(df.info())
print(df.head())

# -------------------------------
# Step 2: Check for Missing Values
# -------------------------------
print("Missing values in each column:")
print(df.isnull().sum())

# -------------------------------
# Step 3: Convert Date and Age Columns
# -------------------------------
# Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Convert 'age' to integer. If there are missing values, fill them with the median first.
df['age'] = df['age'].fillna(df['age'].median()).astype(int)

# -------------------------------
# Step 4: Standardize Text Data
# -------------------------------
# Define the list of text columns that need standardization
text_cols = [
    'manner_of_death', 'armed', 'gender', 'race', 
    'city', 'state', 'threat_level', 'flee', 'arms_category'
]

# Convert text to lowercase and remove extra spaces
df[text_cols] = df[text_cols].apply(lambda col: col.str.lower().str.strip())

# -------------------------------
# Step 5: Remove Duplicate Entries
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# Final Check and Save the Cleaned Data
# -------------------------------
print("Cleaned Data Info:")
print(df.info())
print(df.head())

# Save the cleaned DataFrame to a new CSV file in your project folder
output_file = "/Users/brayantchidalu/Documents/Data analyst/project 1/cleaned_shootings.csv"
df.to_csv(output_file, index=False)
print("Cleaned data saved to:", output_file)


