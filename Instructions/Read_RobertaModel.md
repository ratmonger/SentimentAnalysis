# IMDb Movie Review Sentiment Analysis with Roberta Model

This Python script demonstrates how to use the Hugging Face Transformers library to perform sentiment analysis on movie reviews using a pre-trained Twitter RoBERTa-based model. It provides a function to analyze the sentiment of a given text and returns the sentiment label and corresponding scores.

## Prerequisites

Before running this script, you need to have the following installed:

- Python
- `transformers` library
- `scipy` library
- A machine with a compatible GPU for better performance (optional)
- A stable internet connection to download the pre-trained model weights

You can install the required libraries using `pip`. Example:

```bash
pip install transformers scipy
```

## Instructions

1. Import the necessary Python libraries at the beginning of your script:

```python
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
```

2. Define two movie reviews, one with a positive rating and one with a negative rating:

```python
positiveRating = "It is no wonder that the film has such a high rating, it is quite literally breathtaking. ..."
negativeRating = "For the life of me, I can't understand all the gushing about this cornball, sentimental and PHONY movie. ..."
```

3. Define a function `analyze_sentiment(text)` to analyze the sentiment of a given text:

```python
def analyze_sentiment(text):
    # Define the pre-trained model
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)

    # Encode the text and get sentiment scores
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # Determine the sentiment label
    sentiment_label = "Neutral"
    if scores[0] > scores[2]:  # If Negative score is greater than Positive score
        sentiment_label = "Negative"
    elif scores[2] > scores[0]:  # If Positive score is greater than Negative score
        sentiment_label = "Positive"

    # Format the scores
    formatted_scores = {
        "Negative": f"{scores[0]:.6f}",
        "Neutral": f"{scores[1]:.6f}",
        "Positive": f"{scores[2]:.6f}"
    }

    # Return the sentiment label and formatted scores
    return sentiment_label, formatted_scores
```

4. Analyze the sentiment of the provided movie reviews using the `analyze_sentiment` function:

```python
# Positive Review
print("Positive Review: " + str(analyze_sentiment(positiveRating)))

# Negative Review
print("Negative Review: " + str(analyze_sentiment(negativeRating)))
```

This script demonstrates how to load a pre-trained model and tokenizer, encode text, and analyze sentiment using the Hugging Face Transformers library. The sentiment label is determined as "Positive," "Neutral," or "Negative" based on the model's output scores.

Feel free to use this script to analyze sentiment in other text data by passing it as an argument to the `analyze_sentiment` function.

**Note:** Ensure that you have a stable internet connection to download the pre-trained model weights when running this script.