import RoBERTA_Go as rbGO
import MovieSubtitle_Parser as msp
import pandas as pd

# senti = rbGO.emotion_analysis("I hate this movie, it sucks!")
# print(senti)
df = (msp.MovSubGetter('../ShawShank_CreatedFiles/The.Shawshank.Redemption_subtitles.srt'))

df['label'] = [i for i in range(1, len(df) + 1)]
df['score'] = [i for i in range(1, len(df) + 1)]

# print(df)
# print(df.iloc[0][0])
sent_score = []
sent_labels = []
sent_tuple = []

# Emotion labels and their respective scores
emotion_labels = [
    'admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring',
    'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval',
    'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief',
    'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization',
    'relief', 'remorse', 'sadness', 'surprise', 'neutral'
]
# Create a dictionary with empty values for each emotion label
emotion_dict = {emotion: [] for emotion in emotion_labels}

# Now, empty_emotion_dict contains empty lists for each emotion label
print(emotion_dict)
# emotion_dict['Admiration'].append(1)
# print(emotion_dict)
# print(sent_tuple[0])

for i in range(len(df)):
    text = df.iloc[i][0]
    emotSent = rbGO.emotion_analysis(text)
    # tup = str(emotSent[0][0]['label'], emotSent[0][0]['score'])
    # print(str(emotSent[0][0]['label']) +": "+ str(emotSent[0][0]['score']))
    # df.at[i, 'i'] = str(str(emotSent[0][0]['label']) +": "+str( emotSent[0][0]['score']))
    x = emotSent[0][0]['label']
    y = emotSent[0][0]['score']
    df.at[i, 'label'] = x
    df.at[i, 'score'] = y
    emotion_dict[f'{x}'].append(y)

# print(df)
# print(emotion_dict['neutral'])

# if not df.empty:
#     # Specify the file path where you want to save the CSV file
#     csv_file_path = "subLines_and_emotions.csv"
#
#     # Save the DataFrame to a CSV file
#     df.to_csv(csv_file_path, index=False)
#
#     print(f"CSV file saved to {csv_file_path}")
# else:
#     print("No reviews to save or an error occurred during scraping.")
