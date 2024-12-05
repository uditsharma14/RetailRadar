from pyserini.search.lucene import LuceneSearcher
import subprocess
from flask import jsonify
import json

def luceneIndexBuilder(directory):
    # Build the Lucene index using subprocess
    cmd = [
            "python", "-m", "pyserini.index.lucene",
            "--collection", "JsonCollection",
            "--input", directory,
            "--index", "index/test",
            "--generator", "DefaultLuceneDocumentGenerator",
            "--threads", "1",
            "--storePositions", "--storeDocvectors", "--storeRaw"
        ]
    subprocess.run(cmd, check=True)
    # Initialize and return the LuceneSearcher with the path to the index
    searcher = LuceneSearcher("index/test")
    return searcher

def makeQuery(searcher,keyword):   
    # Perform a search query
    hits = searcher.search(f'{keyword}')  

    # Print the search results with content
    print(f"Results for query '{keyword}':")
    results = []
    for i, hit in enumerate(hits, start=1):
        # Retrieve the document by ID
        doc = searcher.doc(hit.docid)
        # Check if the document exists, then extract the content
        if doc is not None:
                raw_doc = doc.raw()  # Assume `raw_doc` is JSON-formatted string
                product = extract_fields(raw_doc)  # Convert raw document to a product object
                results.append(product)
        else:
                results.append({"docid": hit.docid, "error": "Document not found"})
    return jsonify({"results": results})            

  # Then pass the searcher to the query function


def extract_fields(raw_doc):
    try:
        doc = json.loads(raw_doc)  # Convert raw string to dictionary
        
        # Extract fields from the top level and the nested "NER" object
        return {
            "product_title": doc["NER"].get("product_title"),
            "product_category": doc["NER"].get("product_category"),
            "star_rating": doc["NER"].get("star_rating"),
            "Popular_Review": doc.get("contents", "")[:500],
        }
    except json.JSONDecodeError:
        return {"error": "Invalid document format"}
    except KeyError as e:
        return {"error": f"Missing key: {e}"}
