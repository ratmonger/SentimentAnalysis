# IMDb Movie Review Scraper to CSV

This Python script is designed to scrape movie reviews from IMDb and create a DataFrame containing the reviews and star ratings. It uses the Selenium library to automate a web browser (Chrome or Firefox) and BeautifulSoup for parsing HTML content.

## Prerequisites

Before using this script, you should have the following installed:

- Python
- ChromeDriver or GeckoDriver, depending on your choice of web browser
- Required Python libraries (Selenium, BeautifulSoup, pandas, tqdm)

You can install these libraries using `pip`. Example:

```bash
pip install selenium beautifulsoup4 pandas tqdm


## Instructions

1. Import the necessary Python libraries at the beginning of your script:

```python
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
from bs4 import BeautifulSoup
```

2. Define the IMDb movie review URL you want to scrape. Three example URLs are provided in the script, and you can uncomment one of them or use your own URL:

```python
url = "https://www.imdb.com/title/tt0111161/reviews"  # IMDb movie review URL
#url = "https://www.imdb.com/title/tt0111161/reviews?sort=reviewVolume&dir=desc&ratingFilter=0"  # Prolific Reviewers
#url = "https://www.imdb.com/title/tt0111161/reviews?sort=curated&dir=desc&ratingFilter=0"  # Featured Reviewers
```

3. Set the `MAX_REVIEWS` constant to the desired maximum number of reviews to retrieve:

```python
MAX_REVIEWS = 5  # Set to the desired maximum number
```

4. Initialize a WebDriver for your chosen web browser (Chrome or Firefox):

```python
driver = webdriver.Chrome()  # You can also use GeckoDriver for Firefox
```

5. Open the IMDb URL in the web browser:

```python
driver.get(url)
```

6. Scroll down to load more reviews. IMDb loads 25 reviews per scroll, so adjust the number of scrolls based on your `MAX_REVIEWS`:

```python
for _ in range(MAX_REVIEWS // 25):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)  # Sleep to allow the reviews to load
```

7. Initialize a progress bar using `tqdm`:

```python
with tqdm(total=MAX_REVIEWS, desc="Fetching Reviews") as pbar:
```

8. Find and click the "Load More" button until the desired number of reviews is reached:

```python
while len(driver.find_elements(By.ID, "load-more-trigger")) > 0 and len(driver.find_elements(By.CLASS_NAME, "text.show-more__control")) < MAX_REVIEWS:
    # Find the "Load More" button and click it
    load_more_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "load-more-trigger"))
    )
    load_more_button.click()
    time.sleep(2)  # Sleep to allow the reviews to load
    pbar.update(25)  # Increment the progress bar by 25
```

9. Parse the loaded HTML content and close the WebDriver:

```python
page_source = driver.page_source
driver.quit()  # Close the WebDriver
```

10. Use BeautifulSoup to parse the HTML:

```python
soup = BeautifulSoup(page_source, "html.parser")
```

11. Extract review elements and ratings:

```python
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
```

12. Create a pandas DataFrame with two columns: "Review" and "Star Rating":

```python
data = {"Review": reviews, "Star Rating": star_ratings}
reviews_df = pd.DataFrame(data)
```

13. Finally, you can print the DataFrame and save it to a CSV file if desired:

```python
print(reviews_df)
# Your code to scrape reviews and create the reviews_df DataFrame
```

Uncomment the following code to save the DataFrame to a CSV file:

```python
# Check if there are reviews in the DataFrame and no errors
if not reviews_df.empty:
    # Specify the file path where you want to save the CSV file
    csv_file_path = "movie_reviews.csv"
    
    # Save the DataFrame to a CSV file
    reviews_df.to_csv(csv_file_path, index=False)
    
    print(f"CSV file saved to {csv_file_path}")
else:
    print("No reviews to save or an error occurred during scraping.")
```

This script can help you scrape IMDb movie reviews and save them as a DataFrame for further analysis or storage.
```

