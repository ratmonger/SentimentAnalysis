import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

# Check if a GPU is available and use it
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# To check if the GPU is running
# print(device) # If "cuda" prints than GPU else cpu

# Load the tokenizer and model
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.to(device)  # Move the model to the GPU

# Positive Review
def analyze_sentiment(text):
    # Tokenize the input text using the tokenizer:
    # - 'text': The input text to be tokenized.
    # - 'return_tensors': Return the tokenized text as PyTorch tensors.
    # - 'truncation': Ensure that the tokenized text does not exceed a maximum length.
    # - 'padding': Add padding tokens to make sure all sequences have the same length.
    # - 'max_length': Set the maximum length of the tokenized text (adjust as needed).
    encoded_text = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=128)

    # Move the tokenized text tensors to the GPU for faster computation:
    # - 'key: val' pairs are unpacked from the encoded_text dictionary, and each tensor is moved to the GPU.
    encoded_text = {key: val.to(device) for key, val in encoded_text.items()}

    # Pass the tokenized input through the model to get sentiment scores:
    # - 'output' contains the model's output, including sentiment scores.
    output = model(**encoded_text)

    # Extract the sentiment scores and convert them to a NumPy array:
    # - 'scores' contains the sentiment scores for the input text.
    scores = output.logits[0].detach().cpu().numpy()

    # Apply the softmax function to obtain normalized scores:
    # - The softmax function converts the raw scores into probabilities for different sentiment labels.
    scores = softmax(scores)

    sentiment_label = "Neutral"
    if scores[0] > scores[2]:
        sentiment_label = "Negative"
    elif scores[2] > scores[0]:
        sentiment_label = "Positive"

    formatted_scores = {
        "Negative": f"{scores[0]:.6f}",
        "Neutral": f"{scores[1]:.6f}",
        "Positive": f"{scores[2]:.6f}"
    }

    return sentiment_label, formatted_scores

#print("Positive Review: " + str(analyze_sentiment(positiveRating)))
#print(analyze_sentiment("I hate this movie"))
