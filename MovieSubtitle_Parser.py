import re
import pandas as pd
from bs4 import BeautifulSoup

def parse_subtitle(subtitle_text, max_characters_per_block=250):
    lines = subtitle_text.split('\n')

    data = []
    current_block = ""

    for line in lines:
        # Remove HTML tags using BeautifulSoup
        line = BeautifulSoup(line, 'html.parser').text

        # List of characters you want to remove
        characters_to_remove = [
            '{\\an8}',           # Lines starting with {\an8}
            '\\\\an8-}',         # Lines starting with {\an8-}
            '\\an8--}',          # Lines starting with {\an8--}
            '\\\\an8}',          # Lines starting with {\\\an8}
            '\\\\an8}\\.\\.\\.',  # Lines starting with {\an8}...
            '{\\an8}...',        # Additional pattern to remove
        ]

        for character in characters_to_remove:
            line = line.replace(character, "")

        if line.strip() == "":
            continue  # Skip lines that become empty after removal

        if not re.match(r'\d+', line):
            current_block += line

        else:
            if current_block:
                data.append(current_block.strip())
            current_block = ""

    # Add the last block if it exists
    if current_block:
        data.append(current_block.strip())

    # Split blocks into chunks of max_characters_per_block
    blocks = [block[i:i+max_characters_per_block] for block in data for i in range(0, len(block), max_characters_per_block)]

    # Create DataFrame
    df = pd.DataFrame(blocks, columns=['Subtitle Block'])

    return df

# Read subtitle text from a file
file_path = 'ShawShank_CreatedFiles/The.Shawshank.Redemption_subtitles.srt'  # Replace with your file path
with open(file_path, 'r', encoding='utf-8') as file:
    subtitle_text = file.read()

result_df = parse_subtitle(subtitle_text)
print(result_df)
