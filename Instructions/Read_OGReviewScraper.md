
# Web Scraping IMDb Movie Reviews

This Python script demonstrates how to scrape movie reviews from IMDb using the `requests` library and parse the reviews using `BeautifulSoup`. It retrieves a specified number of movie reviews from IMDb and stores them in a pandas DataFrame.

## Prerequisites

Before running this script, you need to have the following installed:

- Python
- `requests` library
- `bs4` (Beautiful Soup) library
- `pandas` library

You can install the required libraries using `pip`. Example:

```bash
pip install requests beautifulsoup4 pandas
```

## Instructions

1. Import the necessary Python libraries at the beginning of your script:

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

2. Set the IMDb movie review URL you want to scrape and specify the maximum number of reviews to retrieve:

```python
url = "https://www.imdb.com/title/tt0111161/reviews"
MAX_REVIEWS = 10  # Set to the desired maximum number of reviews
```

3. Create empty lists to store reviews and star ratings:

```python
reviews = []
star_ratings = []
```

4. Send an initial HTTP request to the review page and start a loop to retrieve reviews. The loop will continue until it reaches the maximum number of reviews or there are no more reviews to load:

```python
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

    # Extract the next page URL and continue the loop
    page_number += 1
    next_page_url = f"{url}?sort=review_date&dir=desc&ratingFilter=0&page={page_number}"
    response = requests.get(next_page_url)
```

5. Create a pandas DataFrame with two columns: "Review" and "Star Rating" and print the DataFrame:

```python
data = {"Review": reviews, "Star Rating": star_ratings}
reviews_df = pd.DataFrame(data)

# Print the DataFrame
print(reviews_df)
```

This script demonstrates how to scrape and retrieve movie reviews from IMDb and store them in a structured format for further analysis. You can customize the IMDb URL and the maximum number of reviews to retrieve according to your needs.

Feel free to use this script to scrape and analyze reviews from other web pages by changing the URL in the `url` variable.
