from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment Analyzer
tool = SentimentIntensityAnalyzer()

# Sample text
text = "It is a sunny day but it might rain later"

# Perform Sentiment Analysis
sentiment_score = tool.polarity_scores(text)

# Print sentiment scores
print("Sentiment Score : ",sentiment_score)