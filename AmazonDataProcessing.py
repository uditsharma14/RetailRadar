import pandas as pd
import numpy as np

# Load the dataset with error handling for bad lines
file_path = '/Users/uditsharma/Amazon_Review_dateset/amazon_reviews_us_Personal_Care_Appliances_v1_00.tsv'
data = pd.read_csv(file_path, sep='\t', on_bad_lines='skip')

# Preview the dataset


'''Index(['marketplace', 'customer_id', 'review_id', 'product_id',
       'product_parent', 'product_title', 'product_category', 'star_rating',
       'helpful_votes', 'total_votes', 'vine', 'verified_purchase',
       'review_headline', 'review_body', 'review_date']'''

print(data.columns)

print(data.head())



# Keep only relevant columns for the analysis
data = data[['marketplace', 'product_id',
       'product_parent', 'product_title', 'product_category', 'star_rating',
       'helpful_votes', 'total_votes', 'verified_purchase',
       'review_headline', 'review_body']]

# Drop rows with any missing values
#data.dropna(inplace=True)

# Convert star ratings to integer
#data['star_rating'] = data['star_rating'].astype(int)

# Check data types and for null values
product_review_counts = data.groupby('product_title').size()
print(product_review_counts)
