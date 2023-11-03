from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

# BEFORE YOU RUN THIS CODE
# You need to install this on your machine terminal
# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Movie: The ShankShaw Redemption
# Review Link: https://www.imdb.com/title/tt0111161/reviews?sort=curated&dir=asc&ratingFilter=0

# 10/10
positiveRating = "It is no wonder that the film has such a high rating, it is quite literally breathtaking. What can I say that hasn't said before? Not much, it's the story, the acting, the premise, but most of all, this movie is about how it makes you feel. Sometimes you watch a film, and can't remember it days later, this film loves with you, once you've seen it, you don't forget. The ultimate story of friendship, of hope, and of life, and overcoming adversity. I understand why so many class this as the best film of all time, it isn't mine, but I get it. If you haven't seen it, or haven't seen it for some time, you need to watch it, it's amazing."
# 1/10
negativeRating = "For the life of me, I can't understand all the gushing about this cornball, sentimental and PHONY movie. There are certainly some strong performances, but they're outweighed by some of the two-dimensional portrayals, weak writing (that opera sequence -- oh, please) and most of all a completely garbage ending (I won't give it away) that stomps on what little credibility the movie has. I guess you really can't go broke under-estimating people's intelligence."
# print(review)


'''
Provide by HuggingFace

This part of the code runs the auto tokenizer in the auto model sequence classification methods and load it from a pre-trained model.

It will pull down the model weights that have been stored. Which is basically transfer learning.
This model was trained on a bunch of twitter comments that were labeled. 

We can use these trained weights and apply it to our datasets 

It stands for a Robust optimized BERT pre-training approach. The researchers
who brought it out believed BERT was 'under-trained' & can be improved by
following the below changes while pre-training:

'''
# MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
# tokenizer = AutoTokenizer.from_pretrained(MODEL)
# model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# # Positive Reviews
# encoded_text = tokenizer(positiveRating, return_tensors='pt')
# output = model(**encoded_text)
# scores = output[0][0].detach().numpy()
# scores = softmax(scores)
# print("Positive Review: "+ positiveRating + "\n" + str(scores))
#
# #Negative Reviews
# encoded_text = tokenizer(negativeRating, return_tensors='pt')
# output = model(**encoded_text)
# scores = output[0][0].detach().numpy()
# scores = softmax(scores)
# print("Negative Review: " + negativeRating + "\n" + str(scores))

def analyze_sentiment(text):
    # Define the pre-trained model
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)

    # Encode the text and get sentiment scores
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # Determine the sentiment label
    sentiment_label = "Neutral"
    if scores[0] > scores[2]:  # If Negative score is greater than Positive score
        sentiment_label = "Negative"
    elif scores[2] > scores[0]:  # If Positive score is greater than Negative score
        sentiment_label = "Positive"

    # Format the scores
    formatted_scores = {
        "Negative": f"{scores[0]:.6f}",
        "Neutral": f"{scores[1]:.6f}",
        "Positive": f"{scores[2]:.6f}"
    }

    # Return the sentiment label and formatted scores
    return sentiment_label, formatted_scores

# Positive Review
print("Positive Review: " + str(analyze_sentiment(positiveRating)))

# Negative Review
print("Negative Review: " + str(analyze_sentiment(negativeRating)))