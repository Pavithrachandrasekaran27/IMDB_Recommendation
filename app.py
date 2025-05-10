import streamlit as st
from recommendation_engine import MovieRecommender

st.title("🎬 IMDb Movie Recommendation System (2024)")
st.subheader("Enter a movie storyline to get similar recommendations")

input_story = st.text_area("✍️ Enter Storyline Here:")

if st.button("Get Recommendations"):
    if input_story.strip():
        recommender = MovieRecommender("movies_2024.csv")
        recommendations = recommender.recommend(input_story)
        st.subheader("📽 Top 5 Recommended Movies")
        for idx, row in recommendations.iterrows():
            st.write(f"**🎞 {row['Movie Name']}**")
            st.write(f"📝 {row['Storyline']}")
            st.markdown("---")
    else:
        st.error("Please enter a storyline.")
