from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tqdm import tqdm

# IMDb movie review URL
url = "https://www.imdb.com/title/tt0111161/reviews/"

# Initialize a WebDriver (make sure you have ChromeDriver or GeckoDriver installed)
driver = webdriver.Chrome()  # You can also use GeckoDriver for Firefox

# Open the IMDb URL in the browser
driver.get(url)

# Function to click the "Load More" button
def click_load_more():
    try:
        load_more_button = driver.find_element(By.ID, "load-more-trigger")
        load_more_button.click()
        return True
    except Exception as e:
        #print(f"Error clicking 'Load More' button: {e}")
        return False

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Sleep to allow the reviews to load





# Specify the desired number of reviews to fetch
desired_reviews = 100  # Change this number to your desired value

# Click the "Load More" button until the desired number of reviews is reached
with tqdm(total=desired_reviews, desc="Fetching Reviews") as pbar:
    while len(driver.find_elements(By.ID, "load-more-trigger")) > 0 and len(driver.find_elements(By.CLASS_NAME, "text.show-more__control")) < desired_reviews:
        success = click_load_more()
        if success:
            time.sleep(2)  # Sleep to allow the reviews to load
            pbar.update(25)  # Increment the progress bar by 25 (IMDb loads 25 reviews per scroll)

# Extract review elements and star ratings
review_elements = driver.find_elements(By.CLASS_NAME, "text.show-more__control")
rating_elements = driver.find_elements(By.CLASS_NAME, "ipl-ratings-bar")

# Extract review text and star ratings
reviews = [review.text for review in review_elements]
ratings = []

for rating in rating_elements:
    try:
        rating_value = rating.find_element(By.CLASS_NAME, "rating-other-user-rating").find_element(By.TAG_NAME, "span").text
    except Exception as e:
        rating_value = None
    ratings.append(rating_value)

# Make sure lengths match
min_length = min(len(reviews), len(ratings))
reviews = reviews[:min_length]
ratings = ratings[:min_length]

# Create a pandas DataFrame only if both review and rating are available
df_data = {"Review": [], "Rating": []}
for review, rating in zip(reviews, ratings):
    if review and rating is not None:
        df_data["Review"].append(review)
        df_data["Rating"].append(rating)

# Create a pandas DataFrame
df = pd.DataFrame(df_data)

# Save the DataFrame to a CSV file
csv_file_path = f"imdb_reviews_with_ratings_{df.shape[0]}.csv"
df.to_csv(csv_file_path, index=False)
print(f"CSV file saved to {csv_file_path}")

# Close the WebDriver
driver.quit()
