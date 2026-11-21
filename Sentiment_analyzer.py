# Simple Rule-Based Sentiment Analyzer (Beginner NLP Project)

positive_words = ["good", "great", "awesome", "happy", "love", "excellent", "amazing", "best"]
negative_words = ["bad", "sad", "terrible", "hate", "worst", "awful", "boring", "angry"]

def analyze_sentiment(text):
    words = text.lower().split()
    pos_score = sum(1 for word in words if word.strip(".,!?") in positive_words)
    neg_score = sum(1 for word in words if word.strip(".,!?") in negative_words)

    if pos_score > neg_score:
        return "Positive Sentiment 😊"
    elif neg_score > pos_score:
        return "Negative Sentiment 😞"
    else:
        return "Neutral Sentiment 😐"

print("--- AI Sentiment Analyzer ---")
user_input = input("Enter a sentence or review: ")
print("Result:", analyze_sentiment(user_input))