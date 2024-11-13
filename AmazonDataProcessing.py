import os
import pandas as pd
from AmazonSentimentAnalsys import get_sentiment
from LuceneReviewProcesser import luceneIndexBuilder, makeQuery
from VisualRepresentation import create_bar_graph_for_top_5, create_pie_for_review_sentiment, create_bar_graph_for_top_10_products, create_dual_axis_bar_chart

# Load the dataset with error handling for bad lines
file_path = '/Users/uditsharma/Downloads/amazon_reviews_us_Personal_Care_Appliances_v1_00.tsv'
data = pd.read_csv(file_path, sep='\t', on_bad_lines='skip')

# Preview the dataset
'''Index(['marketplace', 'customer_id', 'review_id', 'product_id',
       'product_parent', 'product_title', 'product_category', 'star_rating',
       'helpful_votes', 'total_votes', 'vine', 'verified_purchase',
       'review_headline', 'review_body', 'review_date']'''

# Keep only relevant columns for the analysis
data = data[['marketplace', 'product_id',
       'product_parent', 'product_title', 'product_category', 'star_rating',
       'helpful_votes', 'total_votes', 'verified_purchase',
       'review_headline', 'review_body']]


# Apply the function to each review
data[['compound_score', 'sentiment']] = data['review_body'].apply(get_sentiment).apply(pd.Series)

# Generate the `contents` field by concatenating title, headline, and body
data_to_index = pd.DataFrame({
    'id': data.index.astype(str),  # Unique ID based on the index of `data`
    'contents': data['product_title'] + ' ' + data['review_headline'] + ' ' + data['review_body']  # Concatenated contents
})

# Define the `NER` field by applying a function that creates a dictionary for each row
data_to_index['NER'] = data.apply(lambda row: {
    'marketplace': row['marketplace'],
    'product_id': row['product_id'],
    'product_parent': row['product_parent'],
    'product_title': row['product_title'],
    'product_category': row['product_category'],
    'star_rating': row['star_rating'],
    'helpful_votes': row['helpful_votes'],
    'total_votes': row['total_votes'],
    'verified_purchase': row['verified_purchase']
}, axis=1)

data_json = data_to_index.to_json(orient='records', lines=True)
# Define the directory path and file name
directory = 'test'
file_path = os.path.join(directory, 'data_to_index.json')
# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Save the JSON output to the file inside the 'text' directory
with open(file_path, 'w') as f:
    f.write(data_json)

print(f"JSON file has been saved to {file_path}.")
# Usage
searcher = luceneIndexBuilder(directory)  # First build the index and get the searcher
makeQuery(searcher)


# Unified Product Search function
def search_product(keyword, df):
    # Filter products containing the keyword in title or body
    results = df[df['product_title'].str.contains(keyword, case=False, na=False)]
    return results[['product_id', 'product_title', 'review_body', 'sentiment', 'compound_score']]

# Intelligent Comparison function
def intelligent_comparison(product_id, df):
    # Filter reviews for the specified product
    product_reviews = df[df['product_id'] == product_id]
    avg_sentiment_score = product_reviews['compound_score'].mean()
    avg_rating = product_reviews['star_rating'].mean()
    return {"avg_sentiment_score": avg_sentiment_score, "avg_rating": avg_rating}

def search_and_rank_products(keyword, df):
    # Filter products based on keyword in product title
    matched_products = df[df['product_title'].str.contains(keyword, case=False, na=False)]

    # Group by product_id and calculate average sentiment score and average rating
    ranked_products = matched_products.groupby('product_id', as_index=False).apply(
        lambda x: pd.Series({
            'product_id': x['product_id'].iloc[0],  # Include product_id in the Series
            'product_title': x['product_title'].iloc[0],
            'avg_sentiment_score': x['compound_score'].mean(),
            'avg_rating': x['star_rating'].mean()
        })
    ).reset_index(drop=True)

    # Sort by avg_sentiment_score and avg_rating, return top 10
    ranked_products = ranked_products.sort_values(
        ['avg_sentiment_score', 'avg_rating'], ascending=False
    ).head(10)
    
    return ranked_products[['product_id', 'product_title', 'avg_sentiment_score', 'avg_rating']]

def main():
    print("Welcome to RetailRadar Insight!")
    action = input("Choose an action: (1) Search Products, (2) Compare Products, (3) Top Ranked Products by Keyword: ")

    if action == '1':
        keyword = input("Enter product name or keyword to search: ")
        results = search_product(keyword, data)
        print("Search Results:\n", results)
    elif action == '2':
        product_id = input("Enter the Product ID for comparison: ")
        comparison_result = intelligent_comparison(product_id, data)
        print(f"Comparison Results for Product ID {product_id}:")
        print(f"Average Sentiment Score: {comparison_result['avg_sentiment_score']}")
        print(f"Average Rating: {comparison_result['avg_rating']}")
    elif action == '3':
        keyword = input("Enter a keyword to find top-ranked products: ")
        top_ranked_products = search_and_rank_products(keyword, data)
        print("Top 10 Ranked Products:\n", top_ranked_products)
        create_bar_graph_for_top_10_products(top_ranked_products)
        create_dual_axis_bar_chart(top_ranked_products)
    else:
        print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
    #create_pie_for_review_sentiment(data)
    #create_bar_graph_for_top_5(data)


