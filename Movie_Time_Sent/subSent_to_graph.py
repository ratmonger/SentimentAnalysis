import matplotlib.pyplot as plt
import pandas as pd

# Emotion labels and their respective scores
emotion_labels = [
    'admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring',
    'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval',
    'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief',
    'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization',
    'relief', 'remorse', 'sadness', 'surprise', 'neutral'
]

# Create a dictionary with empty lists for each emotion label
emotion_dict = {emotion: [] for emotion in emotion_labels}

# Path to the CSV file
file_path = 'subLines_and_emotions.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Iterate through the DataFrame rows to populate emotion_dict
for i in range(len(df)):
    x = df.iloc[i][1]  # Emotion label
    y = df.iloc[i][2]  # Sentiment score
    emotion_dict[f'{x}'].append(y)  # Append the score to the corresponding emotion

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 6))

# List of emotions to check for plotting
emotions_to_check = ['sadness', 'anger', 'joy', 'fear', 'surprise']

# Iterate through emotion_dict and plot the selected emotions
for emotion, scores in emotion_dict.items():
    if emotion in emotions_to_check:
        ax.plot(range(len(scores)), scores, label=f'{emotion.capitalize()} Sentiment Score')
    else:
        continue  # Skip emotions not in emotions_to_check

# Set labels and title for the plot
ax.set_xlabel('Line Number (i)')
ax.set_ylabel('Sentiment Score')
ax.set_title('Sentiment Scores vs. Line Number')

# Show the legend
ax.legend()

# Display the plot
plt.show()
