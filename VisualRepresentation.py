
import matplotlib.pyplot as plt
import textwrap

def create_pie_for_review_sentiment(data):
    # Plotting the pie chart
    plt.figure(figsize=(8, 8))
    sentiment_counts = data['sentiment'].value_counts()
    plt.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct='%1.1f%%',    # Show percentage with one decimal place
    startangle=140,       # Rotate start angle for better view
    colors=['#66c2a5', '#fc8d62', '#8da0cb'],  # Custom colors for positive, negative, neutral
    explode=(0.05, 0.05, 0.05)   # Separate slices slightly for emphasis
    )
    plt.title('Personal Care Appliances Reviews Distribution')
    plt.show()

def create_bar_graph_for_top_5(data):
    average_sentiment = data.groupby('product_title')['compound_score'].mean()
    # Sort by average sentiment in descending order and select the top 5 products
    top_5_products = average_sentiment.sort_values(ascending=False).head(5)
    plt.figure(figsize=(15, 10))
    colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
    top_5_products.plot(kind='bar', color=colors)

    # Adding labels and title
    plt.xlabel('Product Title')
    plt.ylabel('Average Sentiment Score')
    plt.title('Top 5 Products by Average Sentiment Score')
    labels = [textwrap.fill(label, width=15) for label in top_5_products.index]  # Adjust 'width' as needed
    plt.xticks(range(len(labels)), labels, rotation=0, ha='right')
    # Rotate x-axis labels for better readability
    plt.show()
