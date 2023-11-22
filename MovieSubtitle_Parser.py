import re
import pandas as pd
from bs4 import BeautifulSoup
import RobertaModel as RB
import matplotlib.pyplot as plt

def parse_subtitle(subtitle_text, max_characters_per_block=250):
    lines = subtitle_text.split('\n')

    data = []
    current_block = ""

    for line in lines:
        # Remove HTML tags using BeautifulSoup
        line = BeautifulSoup(line, 'html.parser').text

        # List of characters you want to remove
        characters_to_remove = [
            '{\\an8}',           # Lines starting with {\an8}
            '\\\\an8-}',         # Lines starting with {\an8-}
            '\\an8--}',          # Lines starting with {\an8--}
            '\\\\an8}',          # Lines starting with {\\\an8}
            '\\\\an8}\\.\\.\\.',  # Lines starting with {\an8}...
            '{\\an8}...',        # Additional pattern to remove
        ]

        for character in characters_to_remove:
            line = line.replace(character, "")

        if line.strip() == "":
            continue  # Skip lines that become empty after removal

        if not re.match(r'\d+', line):
            current_block += line

        else:
            if current_block:
                data.append(current_block.strip())
            current_block = ""

    # Add the last block if it exists
    if current_block:
        data.append(current_block.strip())

    # Split blocks into chunks of max_characters_per_block
    blocks = [block[i:i+max_characters_per_block] for block in data for i in range(0, len(block), max_characters_per_block)]

    # Create DataFrame
    df = pd.DataFrame(blocks, columns=['Subtitle Block'])

    return df

# Read subtitle text from a file
file_path = 'ShawShank_CreatedFiles/The.Shawshank.Redemption_subtitles.srt'  # Replace with your file path
with open(file_path, 'r', encoding='utf-8') as file:
    subtitle_text = file.read()

tuples = []

result_df = parse_subtitle(subtitle_text)
# print(result_df)
for i, review in result_df.iterrows():
    if i == 10:
        break
    # print(review["Subtitle Block"])
    tuples.append([review["Subtitle Block"], RB.analyze_sentiment(review["Subtitle Block"])])
    print(tuples[i])

import matplotlib.pyplot as plt
import numpy as np

# Assuming `tuples` contains your data as shown in your code
# Extract sentiment scores
sentiment_scores = [item[1][1]['Negative'] for item in tuples]

# Create a scatter plot with adjusted horizontal spacing
x_values = np.arange(0, len(sentiment_scores) * 2, step=2)  # Increase the step size
plt.scatter(x_values, sentiment_scores, c='blue', marker='o')
plt.xlabel('Review Index')
plt.ylabel('Negative Sentiment Score')
plt.title('Negative Sentiment Scores by Review Index')
plt.grid(True)

# Set y-axis limits to cover a wider range (e.g., from 0 to 1.2)
plt.ylim(0, 1.2)

plt.show()




