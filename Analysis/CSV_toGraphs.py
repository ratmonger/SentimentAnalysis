import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
file_path = 'modified_movie_reviews_700_test.csv'  # Replace with the actual file path
df = pd.read_csv(file_path)

# Count the number of reviews for each sentiment
sentiment_counts = df['Sentiment'].value_counts()

# Plot the bar graph
plt.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'red'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')

# Show the plot
plt.show()
