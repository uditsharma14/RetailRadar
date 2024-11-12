from pyserini.search.lucene import LuceneSearcher  # Adjusted import
import os
import os
import json
import subprocess
from pyserini.index.lucene import LuceneIndexer

def   main(): 
    # Create a directory to store the index
    index_dir = 'index' 
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    # Create some sample documents


# Sample documents
    documents = [
        {'id': '1', 'contents': 'Lucene is a powerful search library.'},
        {'id': '2', 'contents': 'Pyserini is a Python wrapper for Lucene.'},
        { "id": "3", "contents": "Project and its atomic bomb helped bring an end to World War II. Its legacy of peaceful uses of atomic energy continues to have an impact on history and science.",
          "NER": {
            "ORG": ["The Manhattan Project"],
            "MONEY": ["World War II"]
         }
         }]

    # Create a directory to store the JSON files if it doesn't exist
    if not os.path.exists("test"):
        os.mkdir("test")

    # Iterate through the documents and save each to a separate JSON file
    for i, doc in enumerate(documents, 1):  # Start index at 1
        with open(os.path.join("test", f"doc{i}.json"), 'w') as out:
            json.dump(doc, out, indent=4)  # Pretty print with indent

    print("Documents saved successfully.")

        

    cmd = [
            "python", "-m", "pyserini.index.lucene",
            "--collection", "JsonCollection",
            "--input", "test",
            "--index","index/test",
            "--generator", "DefaultLuceneDocumentGenerator",
            "--threads", "1",
            "--storePositions", "--storeDocvectors", "--storeRaw"
        ]
    subprocess.run(cmd, check=True)
    # Step 2: Searching the Index
    # Now that we have an index, we can search it using SimpleSearcher.

    # Initialize the SimpleSearcher with the path to the index
    searcher = LuceneSearcher("index/test")

    # Perform a search query
    query = 'The Manhattan Project'
    hits = searcher.search(f'NER_ORG:{query}')
    # Print the search results
    print(f"Results for query '{query}':")
    for i in range(len(hits)):
        print(f'{i+1:2} {hits[i].docid:4} {hits[i].score:.5f}')

      # Perform a search query
    review_query = 'Pyserini'
    hits = searcher.search(f'{review_query}')
    # Print the search results
    print(f"Results for query '{query}':")
    for i in range(len(hits)):
        print(f'{i+1:2} {hits[i].docid:4} {hits[i].score:.5f}')

if __name__ == "__main__":
    main()