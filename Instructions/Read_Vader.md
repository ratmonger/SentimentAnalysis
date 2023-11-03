
# Movie Review Sentiment Analysis with NLTK and VADER

This Python script demonstrates how to perform sentiment analysis on movie reviews using the Natural Language Toolkit (NLTK) and the VADER sentiment analysis tool. It tokenizes the reviews, performs part-of-speech tagging, creates named entity chunks, and calculates sentiment scores.

## Prerequisites

Before running this script, you need to have the following installed:

- Python
- `pandas` library
- `numpy` library
- `matplotlib` library
- `seaborn` library
- `nltk` library
- Uncomment the following lines to download NLTK data (run once):

```python
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('vader_lexicon')
```

You can install the required libraries using `pip`. Example:

```bash
pip install pandas numpy matplotlib seaborn nltk
```

## Instructions

1. Import the necessary Python libraries at the beginning of your script:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
```

2. Set the style for plotting using `plt.style.use('ggplot')`.

3. Define two movie reviews, one with a positive rating and one with a negative rating:

```python
positiveRating = "It is no wonder that the film has such a high rating, it is quite literally breathtaking. ..."
negativeRating = "For the life of me, I can't understand all the gushing about this cornball, sentimental and PHONY movie. ..."
```

4. Tokenize the positive review using `nltk.word_tokenize()`:

```python
tokens = nltk.word_tokenize(positiveRating)
```

5. Optionally, you can print the first 10 tokens by uncommenting the following lines:

```python
#print("Tokens:")
#print(tokens[:10])
```

6. Perform part-of-speech tagging using `nltk.pos_tag()`:

```python
tags = nltk.pos_tag(tokens)
```

7. Optionally, you can print the first 10 tags by uncommenting the following lines:

```python
#print("Tags:")
#print(tags[:10])
```

8. Create named entity chunks using `nltk.chunk.ne_chunk()`:

```python
entities = nltk.chunk.ne_chunk(tags)
```

9. Optionally, you can print the named entities by uncommenting the following lines:

```python
#print("Chunking entities:")
#nltk.pprint(entities)
```

10. Create a Sentiment Analyzer object using `SentimentIntensityAnalyzer()`:

```python
sia = SentimentIntensityAnalyzer()
```

11. Analyze sentiment for both positive and negative movie reviews using `sia.polarity_scores()`:

```python
sia_score1 = sia.polarity_scores(positiveRating)
sia_score2 = sia.polarity_scores(negativeRating)
```

12. Print the positive review, its sentiment scores, the negative review, and its sentiment scores:

```python
print(positiveRating)
print("SIA score for Positive Rating: " + str(sia_score1))
print("\n" + negativeRating)
print("SIA score for Negative Rating: " + str(sia_score2))
```

This script demonstrates how to tokenize text, perform part-of-speech tagging, create named entity chunks, and analyze sentiment using VADER sentiment analysis. The sentiment scores include values for positive, negative, neutral, and a compound score.

You can use this script to perform sentiment analysis on other text data as well by replacing the provided movie reviews with your text.
```

Feel free to customize this Markdown file further or add any additional information you think is necessary.