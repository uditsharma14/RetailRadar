from AmazonDataProcessing import prepare_data
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


from AmazonDataProcessing import search_handler

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

def initialize():
    prepare_data()


@app.route('/search', methods=['GET'])
@cross_origin()
def search():
    # Retrieve query parameters
    query = request.args.get('query')
    category = request.args.get('category')
    if not query :
        return jsonify({"error": "Missing required parameters: query "}), 400    
    # Fetch results based on the category
    results = search_handler(query)
    return results

if __name__ == '__main__':
    initialize() 
    app.run(debug=True)
