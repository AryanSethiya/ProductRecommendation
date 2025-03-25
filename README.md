# recomMate - AI-Powered Product Recommendation System

🚀 **recomMate** is an AI-powered product recommendation system that helps users find relevant products based on their search queries using **Sentence-BERT** embeddings and **cosine similarity**.

## 🔥 Features
- **AI-driven recommendations** using `all-MiniLM-L6-v2`
- **Fast and accurate** product search with **cosine similarity**
- **User-friendly web interface** built with Flask
- **Efficient product embeddings storage** using pandas & pickle

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: Sentence-BERT (`sentence-transformers`), scikit-learn
- **Data Handling**: Pandas
- **Web Deployment**: Render.com

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/recomMate.git
cd recomMate
```
### 2️⃣ Create & activate a virtual environment
```bash

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install dependencies
```bash

pip install -r requirements.txt
```
### 4️⃣ Run the Flask app
```bash

python main.py
``` 
The app will start on http://127.0.0.1:5000/.

### 🌍 Live Demo
Try it live: recomMate on Render

### 📂 Project Structure
```bash

recomMate/
│── templates/           # HTML Templates
│   ├── index.html       # Main UI for search
│── main.py              # Flask app
│── product_embeddings.pkl  # Precomputed product embeddings
│── requirements.txt      # Dependencies
│── README.md            # Documentation
```


### 🤖 How It Works
User enters a search query (e.g., "wireless headphones").

The query is converted into an embedding using Sentence-BERT.

Cosine similarity is calculated against precomputed product embeddings.

The top recommendations are returned.



### 📜 License
This project is licensed under the MIT License.

🔥 Made with ❤️ by Aryan Sethiya
