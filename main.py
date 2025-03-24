import os
from flask import Flask, request, render_template
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load a pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the embeddings and product data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
embeddings_path = os.path.join(BASE_DIR, 'product_embeddings.pkl')
df = pd.read_pickle(embeddings_path)

# Ensure 'imgs' column is in list format
df['imgs'] = df['imgs'].apply(lambda x: eval(x) if isinstance(x, str) else x)

app = Flask(__name__, template_folder="templates")

# Function to get recommendations
def recommend_products(query, top_k=10):
    query = query.lower()
    query_embedding = model.encode(query)
    
    # Compute similarity scores
    df['similarity'] = df['embeddings'].apply(lambda x: cosine_similarity([query_embedding], [x]).flatten()[0])
    
    # Sort and return top-k recommendations
    recommendations = df.nlargest(top_k, 'similarity')[['title', 'brand', 'category', 'similarity', 'imgs']]
    return recommendations.to_dict(orient='records')

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        query = request.form['query']
        recommendations = recommend_products(query)

    return render_template('index.html', recommendations=recommendations)

app.secret_key = 'your_secret'

if __name__ == '__main__':
    app.run(debug=True)
