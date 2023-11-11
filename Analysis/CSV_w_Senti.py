import pandas as pd

file_path = 'ShawShank_CreatedFiles/movie_reviews_2000.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Print the first row of the DataFrame
print("First row of the DataFrame:")
print(df.iloc[0])  # Use iloc[0] to get the first row