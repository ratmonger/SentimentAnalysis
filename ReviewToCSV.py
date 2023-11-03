import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm  # Import tqdm for the progress bar

# IMDb movie review URL
url = "https://www.imdb.com/title/tt0111161/reviews"
# Prolific Reviewers
#url = "https://www.imdb.com/title/tt0111161/reviews?sort=reviewVolume&dir=desc&ratingFilter=0"
# Featured Reviewers
#url = "https://www.imdb.com/title/tt0111161/reviews?sort=curated&dir=desc&ratingFilter=0"


# Global constant for the maximum number of reviews to retrieve
MAX_REVIEWS = 5  # Set to the desired maximum number

# Initialize a WebDriver (make sure you have ChromeDriver or GeckoDriver installed)
driver = webdriver.Chrome()  # You can also use GeckoDriver for Firefox

# Open the IMDb URL in the browser
driver.get(url)

# Scroll down to load more reviews
for _ in range(MAX_REVIEWS // 25):  # IMDb loads 25 reviews per scroll
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)  # Sleep to allow the reviews to load

# Initialize tqdm progress bar
with tqdm(total=MAX_REVIEWS, desc="Fetching Reviews") as pbar:
    # Find and click the "Load More" button until the desired number of reviews is reached
    while len(driver.find_elements(By.ID, "load-more-trigger")) > 0 and len(driver.find_elements(By.CLASS_NAME, "text.show-more__control")) < MAX_REVIEWS:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "load-more-trigger"))
        )
        load_more_button.click()
        time.sleep(2)  # Sleep to allow the reviews to load
        pbar.update(25)  # Increment the progress bar by 25

# Parse the loaded HTML content
page_source = driver.page_source
driver.quit()  # Close the WebDriver

# Use BeautifulSoup to parse the HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Extract review elements and ratings
review_elements = soup.find_all("div", class_="text show-more__control")
rating_elements = soup.find_all("span", class_="rating-other-user-rating")

reviews = []
star_ratings = []

for i, review in enumerate(review_elements):
    review_text = review.get_text()
    if i < len(rating_elements):
        rating = rating_elements[i].find("span").get_text(strip=True)
    else:
        rating = "N/A"

    reviews.append(review_text)
    star_ratings.append(rating)

# Create a pandas DataFrame with two columns: "Review" and "Star Rating"
data = {"Review": reviews, "Star Rating": star_ratings}
reviews_df = pd.DataFrame(data)

# Print the DataFrame
print(reviews_df)

# Your code to scrape reviews and create the reviews_df DataFrame
#
# # Check if there are reviews in the DataFrame and no errors
# if not reviews_df.empty:
#     # Specify the file path where you want to save the CSV file
#     csv_file_path = "movie_reviews.csv"
#
#     # Save the DataFrame to a CSV file
#     reviews_df.to_csv(csv_file_path, index=False)
#
#     print(f"CSV file saved to {csv_file_path}")
# else:
#     print("No reviews to save or an error occurred during scraping.")
