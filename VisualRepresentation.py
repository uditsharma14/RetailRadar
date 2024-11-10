
import matplotlib.pyplot as plt
import numpy as np
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

def create_bar_graph_for_top_10_products(ranked_products):
    # Set up plot dimensions
    plt.figure(figsize=(15, 10))
    
    # Bar plot for avg_sentiment_score
    plt.barh(ranked_products['product_title'], ranked_products['avg_sentiment_score'], color='#66c2a5', label='Sentiment Score')
    plt.barh(ranked_products['product_title'], ranked_products['avg_rating'], color='#fc8d62', alpha=0.6, label='Average Rating')

    # Add labels and title
    plt.xlabel('Score')
    plt.title('Top 10 Products by Average Sentiment Score and Average Rating')
    labels = [textwrap.fill(label, width=30) for label in ranked_products['product_title']]
    plt.yticks(range(len(labels)), labels)
    
    # Display legend
    plt.legend()
    plt.show()

def create_dual_axis_bar_chart(data):
    # Extracting data
    product_titles = [textwrap.fill(title, 30) for title in data['product_title']]
    avg_sentiment_scores = data['avg_sentiment_score']
    avg_ratings = data['avg_rating']

    # Create figure and axis
    fig, ax1 = plt.subplots(figsize=(10, 8))

    # Position of bars
    y_pos = np.arange(len(product_titles))

    # Plotting sentiment scores
    ax1.barh(y_pos, avg_sentiment_scores, color='#66c2a5', label='Sentiment Score', height=0.4, align='center')
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(product_titles)
    ax1.invert_yaxis()  # Highest scores at the top
    ax1.set_xlabel('Sentiment Score', color='#66c2a5')
    ax1.tick_params(axis='x', colors='#66c2a5')

    # Setting up second x-axis for ratings
    ax2 = ax1.twiny()
    ax2.barh(y_pos, avg_ratings, color='#fc8d62', label='Average Rating', height=0.4, align='edge')
    ax2.set_xlabel('Average Rating', color='#fc8d62')
    ax2.tick_params(axis='x', colors='#fc8d62')

    # Adding legend
    fig.legend(loc="lower right", bbox_to_anchor=(0.9, 0.1))

    # Title
    plt.title('Top 10 Products by Average Sentiment Score and Average Rating')

    # Show plot
    plt.tight_layout()
    plt.show()

