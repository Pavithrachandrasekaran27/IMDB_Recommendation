import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        
        # Drop empty or whitespace-only storylines
        self.df['Storyline'] = self.df['Storyline'].fillna('').astype(str).str.strip()
        self.df = self.df[self.df['Storyline'].astype(bool)]
        
        if self.df.empty:
            raise ValueError("No valid storylines found in dataset.")
        
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['Storyline'])

    def recommend(self, input_storyline, top_n=5):
        input_vec = self.vectorizer.transform([input_storyline])
        similarity = cosine_similarity(input_vec, self.tfidf_matrix)
        top_indices = similarity[0].argsort()[-top_n:][::-1]
        return self.df.iloc[top_indices][['Movie Name', 'Storyline']]
