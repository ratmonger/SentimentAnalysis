import requests
from bs4 import BeautifulSoup
import pandas as pd

# IMDb movie review URL
url = "https://www.imdb.com/title/tt0111161/reviews"

# Global constant for the maximum number of reviews to retrieve
MAX_REVIEWS = 10  # Set to the desired maximum number

# Create empty lists to store reviews and star ratings
reviews = []
star_ratings = []

# Send an initial HTTP request to the review page
response = requests.get(url)
page_number = 1

while response.status_code == 200 and len(reviews) < MAX_REVIEWS:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and extract review elements
    review_elements = soup.find_all("div", class_="text show-more__control")

    # Extract the star ratings using the specified HTML element
    rating_elements = soup.find_all("span", class_="rating-other-user-rating")

    # Iterate through the review elements and add them to the list
    for i, review in enumerate(review_elements):
        review_text = review.get_text()
        reviews.append(review_text)

        # Extract the star rating if available, otherwise use "N/A"
        if i < len(rating_elements):
            rating = rating_elements[i].find("span").get_text(strip=True)
        else:
            rating = "N/A"
        star_ratings.append(rating)

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

# Create a pandas DataFrame with two columns: "Review" and "Star Rating"
data = {"Review": reviews, "Star Rating": star_ratings}
reviews_df = pd.DataFrame(data)

# Print the DataFrame
print(reviews_df)
