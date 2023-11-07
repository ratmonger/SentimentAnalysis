from bs4 import BeautifulSoup


# Movie Script to Text Blocks
# Later to be put into our sentiment analysis

# Load the HTML file
with open("ShawShank_CreatedFiles/ShawShank RedemptionScript.html", "r") as file:
    html_content = file.read()

# Parse HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Extract the text
script_text = soup.get_text()
print(script_text)

#  Text Processing or Text parsing


