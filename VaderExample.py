# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Uncomment the following lines to download NLTK data (run once)
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('vader_lexicon')

plt.style.use('ggplot')

# Movie: The ShankShaw Redemption
# Review Link: https://www.imdb.com/title/tt0111161/reviews?sort=curated&dir=asc&ratingFilter=0

# 10/10
positiveRating = "It is no wonder that the film has such a high rating, it is quite literally breathtaking. What can I say that hasn't said before? Not much, it's the story, the acting, the premise, but most of all, this movie is about how it makes you feel. Sometimes you watch a film, and can't remember it days later, this film loves with you, once you've seen it, you don't forget. The ultimate story of friendship, of hope, and of life, and overcoming adversity. I understand why so many class this as the best film of all time, it isn't mine, but I get it. If you haven't seen it, or haven't seen it for some time, you need to watch it, it's amazing."
# 1/10
negativeRating = "For the life of me, I can't understand all the gushing about this cornball, sentimental and PHONY movie. There are certainly some strong performances, but they're outweighed by some of the two-dimensional portrayals, weak writing (that opera sequence -- oh, please) and most of all a completely garbage ending (I won't give it away) that stomps on what little credibility the movie has. I guess you really can't go broke under-estimating people's intelligence."
# print(review)

# Tokenize the positive review
tokens = nltk.word_tokenize(positiveRating)

# Uncomment to print the first 10 tokens
#print("Tokens:")
#print(tokens[:10])

# Part-of-speech tagging
tags = nltk.pos_tag(tokens)

# Uncomment to print the first 10 tags
#print("Tags:")
#print(tags[:10])

# Create named entity chunks
entities = nltk.chunk.ne_chunk(tags)

# Uncomment to print the named entities
#print("Chunking entities:")
#nltk.pprint(entities)

'''
VADER (Valence Aware Dictionary and sEntiment Reasoner) - Bag of words approach

Vader: Takes all the words in the sentence and assigns a value of either positive, negative, or neutral to each word.

It sums up all the word values to determine the overall sentiment of the sentence.

Keep in mind that this approach doesn't account for relationships between words, but it's a good start.
'''

# Create a Sentiment Analyzer Object
sia = SentimentIntensityAnalyzer()

# Analyze sentiment for positive and negative movie reviews
sia_score1 = sia.polarity_scores(positiveRating)
sia_score2 = sia.polarity_scores(negativeRating)

# Print the positive review, its sentiment scores, the negative review, and its sentiment scores
print(positiveRating)
print("SIA score for Positive Rating: " + str(sia_score1))
print("\n" + negativeRating)
print("SIA score for Negative Rating: " + str(sia_score2))