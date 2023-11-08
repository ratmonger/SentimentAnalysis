import pandas as pd
import RobertaModel_GPU as RMGPU

# Configuration Variables
MAX_REVIEWS = 500
file_path = 'ShawShank_CreatedFiles/movie_reviews_2000.csv'

# Top 5 Characters in your movie
shawshank_characters = ["Andy Dufresne", "Ellis Red Redding", "Warden Samuel Norton", "Brooks Hatlen", "Tommy Williams"]

def split_flatten_names(character_list):
    """
    Split character names into individual words and flatten the list.

    Parameters:
        character_list (list): A list of character names.

    Returns:
        list: A flattened list of individual words from character names.
    """
    individual_names = [name.split() for name in character_list]
    return [word for name in individual_names for word in name]

# Initialize dictionaries
flattened_names = split_flatten_names(shawshank_characters)
character_sentiments = {character: [] for character in flattened_names}
character_counts = {character: 0 for character in flattened_names}

# Initialize a counter
i = 0
prev_text = None  # Initialize prev_text to None

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Iterate through the reviews in the first column of the DataFrame
for text in df.iloc[:, 0]:
    # Check if the maximum number of reviews has been reached
    if i >= MAX_REVIEWS:
        break

    # Check if each character is mentioned in the text
    for character in flattened_names:
        if character in text:
            # Increment the count of mentions for the current character
            character_counts[character] += 1

            # Check if the current review is different from the previous review
            if text != prev_text:
                # Analyze the sentiment of the current review
                sentiment_result = RMGPU.analyze_sentiment(text)
                # Append the sentiment result to the character's list
                character_sentiments[character].append(sentiment_result)

            # Update prev_text with the current review to avoid duplicate analysis
            prev_text = text

    i += 1

def compute_average_sentiment(results):
    """
    Compute the average sentiment score from a list of sentiment analysis results.

    Parameters:
        results (list): A list of sentiment analysis results for multiple reviews.

    Returns:
        tuple: A tuple containing:
            - The average sentiment label ('Negative', 'Neutral', or 'Positive').
            - A dictionary of average sentiment scores, including 'Negative', 'Neutral', and 'Positive' scores.
    """
    # Initialize variables to accumulate total scores
    total_negative_score = 0
    total_neutral_score = 0
    total_positive_score = 0

    # Iterate through the results to accumulate scores
    for result in results:
        sentiment_label, scores = result
        total_negative_score += float(scores['Negative'])
        total_neutral_score += float(scores['Neutral'])
        total_positive_score += float(scores['Positive'])

    # Calculate the average scores
    num_reviews = len(results)
    average_negative_score = total_negative_score / num_reviews
    average_neutral_score = total_neutral_score / num_reviews
    average_positive_score = total_positive_score / num_reviews

    # Determine the overall sentiment label based on average scores
    if average_negative_score > average_positive_score:
        average_sentiment_label = "Negative"
    elif average_positive_score > average_negative_score:
        average_sentiment_label = "Positive"
    else:
        average_sentiment_label = "Neutral"

    # Create a dictionary of average scores
    average_scores = {
        "Negative": average_negative_score,
        "Neutral": average_neutral_score,
        "Positive": average_positive_score
    }

    # Return the average sentiment label and average scores
    return average_sentiment_label, average_scores

# Create a dictionary to store the average sentiment analysis for each character
average_character_sentiments = {}
for character, sentiment_results in character_sentiments.items():
    if sentiment_results:
        average_sentiment_label, average_sentiment_scores = compute_average_sentiment(sentiment_results)
        average_character_sentiments[character] = {
            "Mentions": len(sentiment_results),
            "AverageSentimentLabel": average_sentiment_label,
            "AverageSentimentScores": average_sentiment_scores
        }

# Print the character counts and average sentiment analysis
for character, count in character_counts.items():
    print(f"{character}: {count}")
    if character in average_character_sentiments:
        print(f"Average Sentiment Analysis for {character}:")
        print(average_character_sentiments[character])
        print()
