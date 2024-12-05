from AmazonDataProcessing import prepare_data
from flask import Flask, request, jsonify

from AmazonDataProcessing import search_handler

app = Flask(__name__)

def initialize():
    prepare_data()

@app.route('/search', methods=['GET'])
def search():
    # Retrieve query parameters
    query = request.args.get('query')
    category = request.args.get('category')
    if not query or not category:
        return jsonify({"error": "Missing required parameters: query and category"}), 400    
    # Fetch results based on the category
    results = search_handler(query)
    return results

if __name__ == '__main__':
    initialize() 
    app.run(debug=True)
