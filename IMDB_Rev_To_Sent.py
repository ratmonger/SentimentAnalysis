import pandas as pd
import RobertaModel_GPU

file_path = 'ShawShank_CreatedFiles/movie_reviews_2000.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

def analyze_reviews(df, max_reviews):
    """
    Analyze sentiment for a set of reviews in a DataFrame.

    Parameters:
        df (DataFrame): The input DataFrame containing reviews.
        max_reviews (int): The maximum number of reviews to process.

    Returns:
        list: A list of sentiment analysis results for the reviews, where each result is a tuple containing:
              - The sentiment label ('Negative', 'Neutral', or 'Positive').
              - A dictionary of sentiment scores, including 'Negative', 'Neutral', and 'Positive' scores.
    """
    # Initialize an empty list to store sentiment analysis results
    rev_to_SentScore = []

    # Initialize a counter to keep track of the number of reviews processed
    i = 0

    # Iterate through the reviews in the first column of the DataFrame
    for text in df.iloc[:, 0]:
        # Check if the maximum number of reviews has been reached
        if i >= max_reviews:
            break

        # Perform sentiment analysis on the current review
        sentiment_score = RobertaModel_GPU.analyze_sentiment(text)

        # Append the sentiment analysis result to the list
        rev_to_SentScore.append(sentiment_score)

        # Increment the counter for each review processed
        i += 1

    # Return the list of sentiment analysis results for the reviews
    return rev_to_SentScore



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





def map_sentiment_to_rating(average_sentiment_score, rating_scale=(1, 10)):
    """
    Map a sentiment score to a movie rating within a specified rating scale.

    Parameters:
        average_sentiment_score (float): The sentiment score to be mapped to a rating.
            This score is typically in the range [-1, 1], where -1 represents a negative sentiment,
            0 represents a neutral sentiment, and 1 represents a positive sentiment.
        rating_scale (tuple): A tuple specifying the range of the movie rating scale.
            It consists of two values: (min_rating, max_rating), where min_rating is the minimum
            rating on the scale, and max_rating is the maximum rating on the scale.

    Returns:
        float: The calculated movie rating based on the sentiment score and the specified rating scale.
    """
    # Extract the minimum and maximum rating from the rating scale
    min_rating, max_rating = rating_scale

    # Normalize the sentiment score to the range [0, 1]
    normalized_sentiment = (average_sentiment_score + 1) / 2

    # Map the normalized sentiment score to the movie rating scale
    # The formula linearly interpolates the normalized sentiment to the rating scale
    movie_rating = min_rating + normalized_sentiment * (max_rating - min_rating)

    return movie_rating







# Example usage:
# MAX_REVIEWS = 1500  # Set the maximum number of reviews to process
# results = analyze_reviews(df, MAX_REVIEWS)
#
#
# # Compute the average sentiment scores
# average_sentiment_label, average_scores = compute_average_sentiment(results)
#
# # Print the average sentiment results
# print("Average Sentiment Label:", average_sentiment_label)
# print("Average Sentiment Scores:", average_scores)


# Example usage
# average_sentiment_score = 0.75  # Replace with the actual average sentiment score
# movie_rating = map_sentiment_to_rating(average_sentiment_score)
# print("Movie Rating:", movie_rating)


MAX_REVIEWS = 1500  # Set the maximum number of reviews to process
results = analyze_reviews(df, MAX_REVIEWS)

# Compute the average sentiment scores
average_sentiment_label, average_scores = compute_average_sentiment(results)

# Print the average sentiment results
print("Average Sentiment Label:", average_sentiment_label)
print("Average Sentiment Scores:", average_scores)

# Calculate the movie rating using map_sentiment_to_rating
rating_scale = (1, 10)  # Define your rating scale here (1 to 10, for example)
movie_rating = map_sentiment_to_rating(average_scores[average_sentiment_label], rating_scale)

# Print the movie rating
print("Movie Rating:", movie_rating)




