import pandas as pd
import RobertaModel_GPU as rbGPU

file_path = 'movie_reviews_700_test.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

custom_values = []  # Replace this list with your custom values
i = 0

for index, row in df.iterrows():
    # Your custom logic to calculate the value based on the row's data
    text = df.iloc[i][0]
    sentiment_label = rbGPU.analyze_sentiment(text)[0]  # Extract the first sentiment label
    custom_values.append(sentiment_label)
    i += 1

df['Sentiment'] = custom_values

# Specify a new file path for the modified DataFrame
output_file_path = 'modified_' + file_path

# Write the modified DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)  # Set index=False to avoid writing row indices to the CSV
