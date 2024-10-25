from textblob import TextBlob
import matplotlib.pyplot as plt



def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity



def plot_sentiment_distribution(sentiment_scores):
    sentiment_categories = [("positive" if score > 0 else 
                           "neutral" if score == 0 else "negative") 
                          for _, score in sentiment_scores]
    
    sentiment_counts = {
        'positive': sentiment_categories.count('positive'),
        'neutral': sentiment_categories.count('neutral'),
        'negative': sentiment_categories.count('negative')
    }

    plt.figure(figsize=(6,6))
    plt.pie(sentiment_counts.values(), 
            labels=sentiment_counts.keys(),
            autopct='%1.1f%%',
            startangle=90,
            colors=['#66b3ff','#99ff99','#ff9999'])
    plt.title("Sentiment Distribution in Customer Calls")
    return plt