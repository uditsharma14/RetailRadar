from pyserini.search.lucene import LuceneSearcher
import subprocess

def luceneIndexBuilder(directory):
    # Build the Lucene index using subprocess
    cmd = [
            "python", "-m", "pyserini.index.lucene",
            "--collection", "JsonCollection",
            "--input", "test",
            "--index", "index/test",
            "--generator", "DefaultLuceneDocumentGenerator",
            "--threads", "1",
            "--storePositions", "--storeDocvectors", "--storeRaw"
        ]
    subprocess.run(cmd, check=True)
    # Initialize and return the LuceneSearcher with the path to the index
    searcher = LuceneSearcher("index/test")
    return searcher

def makeQuery(searcher):   
    # Perform a search query
    query = 'The Manhattan Project'
    hits = searcher.search(f'NER_ORG:{query}')    
    # Print the search results with content
    for i, hit in enumerate(hits, start=1):
        # Retrieve the document by ID
        doc = searcher.doc(hit.docid)
        
        # Check if the document exists, then extract the content
        if doc is not None:
            content = doc.raw()  # `raw()` retrieves the document content as a string
            print(f'{i:2} {hit.docid:4} {hit.score:.5f}\nContent: {content}\n')
        else:
            print(f'{i:2} {hit.docid:4} {hit.score:.5f}\nContent: Document not found\n')

  # Then pass the searcher to the query function
