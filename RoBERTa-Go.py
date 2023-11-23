"""
Sentiment Analysis with Roberta

This Python script uses a pre-trained Roberta-based model for sentiment analysis. The model can recognize 28 different emotions in text, such as happiness, anger, sadness, and more. It assigns a score to each emotion, indicating how likely it is present in a given text.

Usage:
1. Install the necessary libraries:
   - Transformers library by Hugging Face: https://github.com/huggingface/transformers
   - PyTorch (if not already installed)

2. Load the model using Hugging Face's Transformers library:
   from transformers import pipeline

   # Create a sentiment analysis pipeline with the pre-trained Roberta model
   classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

3. Analyze text sentiment:
   sentences = ["I am not having a great day", "I'm so excited!"]

   # Get sentiment analysis results for each sentence
   model_outputs = classifier(sentences)

   # Access the sentiment scores for each emotion in the output
   for output in model_outputs:
       print(output)

4. Threshold for Sentiment:
   By default, a threshold of 0.5 is applied to the sentiment scores. You can consider an emotion as present if its score is above this threshold.

5. Model Accuracy and Improvement:
   Keep in mind that while the model is good at recognizing emotions, it may not be perfect. Its accuracy can be improved by providing more training examples or cleaning up the data used for training.

Please make sure to check the model's license and terms of use, especially if you plan to use it in a commercial application. You can find more information and evaluation metrics in the provided documentation and evaluation notebook.

References:
- Hugging Face Transformers: https://github.com/huggingface/transformers
- Model Repository: https://huggingface.co/SamLowe/roberta-base-go_emotions
- Evaluation Metrics and Notebook: [Link to Evaluation Notebook]

Note: Replace [Link to Evaluation Notebook] with the actual URL for the evaluation notebook, if available.
"""

# Importing the necessary library from Hugging Face's Transformers.
# This library provides tools and pre-trained models for natural language processing (NLP).
# We'll use it to create a sentiment analysis pipeline and work with the Roberta-based model.

# # Import the necessary library from Hugging Face's Transformers
from transformers import pipeline

# Create a sentiment analysis pipeline with the pre-trained Roberta model
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

# List of sentences you want to analyze for sentiment
sentences = ["I am not having a great day", "I'm so excited!"]

# Get sentiment analysis results for each sentence
model_outputs = classifier(sentences)

# Access the sentiment scores for each emotion in the output
# for output in model_outputs:
#     print(output)
print(model_outputs)

import matplotlib.pyplot as plt

# Time range from 1 to 30
time = list(range(1, 31))

# Sentiment scores for selected emotions (you can customize this)
emotions = ['disappointment', 'sadness', 'excitement']
scores = {
    'disappointment': [0.1, 0.15, 0.2, 0.18, 0.12, 0.11, 0.1, 0.09, 0.08, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.18, 0.19, 0.2, 0.22, 0.23, 0.25, 0.28, 0.3, 0.31, 0.32, 0.34, 0.36, 0.38, 0.4],
    'sadness': [0.2, 0.18, 0.15, 0.12, 0.11, 0.1, 0.09, 0.08, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.18, 0.19, 0.2, 0.22, 0.23, 0.25, 0.28, 0.3, 0.31, 0.32, 0.34, 0.36, 0.38, 0.4, 0.45],
    'excitement': [0.05, 0.08, 0.12, 0.16, 0.2, 0.25, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.6]
}

# Create a line chart for each emotion
plt.figure(figsize=(12, 6))
for emotion in emotions:
    plt.plot(time, scores[emotion], label=emotion)

plt.xlabel('Time')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Analysis Over Time')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
