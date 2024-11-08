import pandas as pd
from AmazonSentimentAnalsys import get_sentiment
from VisualRepresentation import create_bar_graph_for_top_5, create_pie_for_review_sentiment

# Load the dataset with error handling for bad lines
file_path = '/Users/uditsharma/Amazon_Review_dateset/amazon_reviews_us_Personal_Care_Appliances_v1_00.tsv'
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
create_pie_for_review_sentiment(data)
create_bar_graph_for_top_5(data)


