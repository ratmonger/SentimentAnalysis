import requests
from bs4 import BeautifulSoup
import pandas as pd
import RobertaModel
from tqdm import tqdm


# IMDb movie review URL
url = "https://www.imdb.com/title/tt0111161/reviews"

# Global constant for the maximum number of reviews to retrieve
MAX_REVIEWS = 20  # Set to the desired maximum number

# Create an empty list to store reviews
reviews = []

# Send an initial HTTP request to the review page
response = requests.get(url)
page_number = 1

while response.status_code == 200 and len(reviews) < MAX_REVIEWS:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and extract review elements
    review_elements = soup.find_all("div", class_="text show-more__control")

    # Iterate through the review elements and add them to the list
    for review in review_elements:
        review_text = review.get_text()
        reviews.append(review_text)

        if len(reviews) >= MAX_REVIEWS:
            break

    # Check if there's a "Load More" button for pagination
    load_more_button = soup.find("button", {"id": "load-more-trigger"})

    if not load_more_button:
        break  # No more reviews to load

    # Extract the next page URL
    page_number += 1
    next_page_url = f"{url}?sort=review_date&dir=desc&ratingFilter=0&page={page_number}"
    response = requests.get(next_page_url)

# Create a pandas DataFrame from the list of reviews
reviews_df = pd.DataFrame({"Review": reviews})

# Print the DataFrame
#print(reviews_df)




'''
Approach 1: For each review, get the sentiment scores, and calculate the final normalized score 
'''
# Initialize dictionaries to store the sums of sentiment scores
total_scores = {'Negative': 0.0, 'Neutral': 0.0, 'Positive': 0.0}

# Create a tqdm instance to display the progress bar
with tqdm(total=len(reviews_df)) as pbar:
    # Iterate through the rows of the DataFrame
    for i, review_text in enumerate(reviews_df["Review"]):
        try:
            sentiment_result = RobertaModel.analyze_sentiment(str(review_text))
            sentiment_scores = sentiment_result[1]  # Extract the dictionary of scores

            # Convert the score values from strings to floats
            sentiment_scores = {key: float(value) for key, value in sentiment_scores.items()}

            # Update the total_scores with the sentiment scores for this review
            for category, score in sentiment_scores.items():
                total_scores[category] += score

            # Increment the progress bar
            pbar.update(1)

        except Exception as e:
            pass
            #print(f"Error analyzing sentiment for Review {i + 1}: {str(e)}")

# Calculate the total sum of scores
total_score = sum(total_scores.values())

# Normalize the final scores by dividing each category's score by the total score
final_normalized_score = {category: score / total_score for category, score in total_scores.items()}

# Print the final normalized score
print("Final Normalized Score:")
print(final_normalized_score)
# The final normalized score is calculated by summing up the sentiment scores for each category (Negative, Neutral, Positive)
# across all reviews and then dividing each category's score by the total sum of scores to obtain a normalized score.