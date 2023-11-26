import RoBERTA_Go as rbGO
import MovieSubtitle_Parser as msp
import pandas as pd

senti = rbGO.emotion_analysis("I hate this movie, it sucks!")
# print(senti)
df = (msp.MovSubGetter('../ShawShank_CreatedFiles/The.Shawshank.Redemption_subtitles.srt'))

df['label'] = [i for i in range(1, len(df) + 1)]
df['score'] = [i for i in range(1, len(df) + 1)]

# print(df)
# print(df.iloc[0][0])
sent_score = []
sent_labels = []

for i in range(len(df)):
    if i == 10:
        break
    text = df.iloc[i][0]
    emotSent = rbGO.emotion_analysis(text)
    # tup = str(emotSent[0][0]['label'], emotSent[0][0]['score'])
    # print(str(emotSent[0][0]['label']) +": "+ str(emotSent[0][0]['score']))
    # df.at[i, 'i'] = str(str(emotSent[0][0]['label']) +": "+str( emotSent[0][0]['score']))
    df.at[i, 'label'] = emotSent[0][0]['label']
    df.at[i, 'score'] = emotSent[0][0]['score']
    sent_labels.append(emotSent[0][0]['label'])
    sent_score.append(emotSent[0][0]['score'])

# print(df)
print("done")
# # Emotion labels and their respective scores
# emotion_labels = [
#     'Admiration', 'Amusement', 'Anger', 'Annoyance', 'Approval', 'Caring',
#     'Confusion', 'Curiosity', 'Desire', 'Disappointment', 'Disapproval',
#     'Disgust', 'Embarrassment', 'Excitement', 'Fear', 'Gratitude', 'Grief',
#     'Joy', 'Love', 'Nervousness', 'Optimism', 'Pride', 'Realization',
#     'Relief', 'Remorse', 'Sadness', 'Surprise', 'Neutral'
# ]

import matplotlib.pyplot as plt

# Assuming you already have df with 'label' and 'score' columns populated
# If not, use the code you provided to populate them

# Emotion labels and their respective scores
emotion_labels = [
    'Admiration', 'Amusement', 'Anger', 'Annoyance', 'Approval', 'Caring',
    'Confusion', 'Curiosity', 'Desire', 'Disappointment', 'Disapproval',
    'Disgust', 'Embarrassment', 'Excitement', 'Fear', 'Gratitude', 'Grief',
    'Joy', 'Love', 'Nervousness', 'Optimism', 'Pride', 'Realization',
    'Relief', 'Remorse', 'Sadness', 'Surprise', 'Neutral'
]


# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 6))  # Adjust the figsize as needed

# Plot the sentiment scores using a line chart
ax.plot(range(10), sent_score, label='Sentiment Score', color='blue', marker='o')

# Set labels and title
ax.set_xlabel('Row Number (i)')
ax.set_ylabel('Sentiment Score')
ax.set_title('Sentiment Scores vs. Row Number')

# Show the plot
plt.tight_layout()  # Ensures labels are not cut off
plt.show()