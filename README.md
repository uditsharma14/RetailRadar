# 🛒 RetailRadar Insight: E-Commerce Sentiment Analytics

**RetailRadar Insight** is an advanced analytics platform that transforms raw Amazon product reviews into actionable consumer insights. By combining **Natural Language Processing (NLP)**, high-performance **Information Retrieval**, and **Data Visualization**, it helps shoppers make informed decisions based on the "vibe" of thousands of reviews—not just star ratings.



## 🌟 Key Features
* **Sentiment-Driven Rankings:** Uses VADER to score reviews from -1.0 (Negative) to +1.0 (Positive).
* **High-Performance Search:** Powered by **Pyserini (Lucene)** to query 85,000+ documents in milliseconds.
* **Intelligent Comparisons:** Compare products based on the delta between their numerical ratings and actual text sentiment.
* **Dynamic Visualizations:** Automated generation of Pie, Bar, and Dual-Axis charts for deep data dives.
* **Modular Architecture:** Clean separation between data processing, indexing, and the Flask/React stack.

---

## 🏗️ System Architecture
The platform is built on a robust Python-based pipeline:

1.  **Data Ingestion:** Cleans and processes Amazon TSV datasets into JSONL format.
2.  **Sentiment Engine:** Analyzes text polarity using the VADER lexicon.
3.  **Indexing Layer:** Builds a Lucene index for efficient keyword-based retrieval.
4.  **API Layer:** A Flask server handles search queries and coordinates with the frontend.
5.  **Frontend:** A modern React application for an intuitive user experience.



---

## 🚀 Getting Started

### Prerequisites
* Python 3.10
* Conda (for environment management)
* Node.js & npm (for the React UI)
* Java 11+ (Required for Pyserini/Lucene)

### 1. Environment Setup
```bash
# Create and activate the virtual environment
conda create -n pyserini python=3.10
conda activate pyserini

# Install core dependencies
pip install flask flask_cors pyserini pandas matplotlib nltk numpy==1.26.4
```

### 2. Clone the Repositories
```bash
# Clone Backend
git clone https://github.com/uditsharma14/RetailRadar.git
cd RetailRadar

# Clone Frontend (into a separate folder)
git clone https://github.com/uditsharma14/retailradar-react-app.git
```

### 3. Initialize the Data & Server
```bash
# Build the Lucene Index
python LuceneReviewProcesser.py

# Start the Flask API
python RetailRadarApp.py
```

### 4. Launch the UI
Open a new terminal:
```bash
cd retailradar-react-app
npm install
npm start
```

---

## 📊 Analytics Deep Dive
RetailRadar provides three primary ways to view data:
* **Search:** Find products by keyword (e.g., "dryer").
* **Compare:** Enter a ProductID to see its average sentiment vs. rating.
* **Top 10:** Visualize the highest-performing products in any category via dual-axis charts.



---

## 🛠️ Built With
* **[Pyserini](https://github.com/castorini/pyserini)** - Lucene toolkit for Python.
* **[VADER](https://github.com/cjhutto/vaderSentiment)** - Sentiment analysis for social media/reviews.
* **[Flask](https://flask.palletsprojects.com/)** - Backend API framework.
* **[React](https://reactjs.org/)** - Frontend UI library.
* **[Matplotlib](https://matplotlib.org/)** - Data visualization.

## 🔮 Future Roadmap
* **Transformer Integration:** Moving from VADER to BERT/RoBERTa for nuanced sentiment.
* **Price Tracking:** Correlating sentiment trends with price fluctuations.
* **Multi-Platform Support:** Expanding datasets to include eBay and Walmart reviews.

Example : 

Fetch and visualize the top-ranked products.

<img width="468" height="452" alt="image" src="https://github.com/user-attachments/assets/cda2db7b-3559-49be-a494-eeec039f3f53" />

</br>

<img width="468" height="298" alt="image" src="https://github.com/user-attachments/assets/63cd7382-d2d8-46a4-b139-bead13f3650e" />




