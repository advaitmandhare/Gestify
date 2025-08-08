import streamlit as st
import nltk
from textblob import TextBlob
from newspaper import Article
import requests

nltk.download('punkt')

# Custom CSS for dark theme with light blue text for the input label
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #000000;
            color: #ffffff;
        }
        .stTextInput label {
            color: #00BFFF; /* Light Blue */
            font-size: 16px;
            font-weight: bold;
        }
        .stTextInput > div > div > input {
            background-color: #222222;
            color: #ffffff;
            border: 1px solid #444444;
            padding: 8px;
            border-radius: 5px;
        }
        .stButton > button {
            background-color: #444444;
            color: #ffffff;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
        }
        .stButton > button:hover {
            background-color: #666666;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def check_url_validity(url):
    return "✅ Trusted" if url.startswith("https://") else "⚠️ Untrusted"

def summarize(url):
    if not url:
        return None, None, None, None, "Invalid URL"
    
    validity_status = check_url_validity(url)
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        
        analysis = TextBlob(article.text)
        polarity = analysis.polarity
        
        if polarity > 0:
            sentiment_text = f"🟢 Positive (Polarity: {polarity:.2f})"
            sentiment_color = "lime"
        elif polarity < 0:
            sentiment_text = f"🔴 Negative (Polarity: {polarity:.2f})"
            sentiment_color = "red"
        else:
            sentiment_text = f"⚪ Neutral (Polarity: {polarity:.2f})"
            sentiment_color = "gray"
        
        return article.title, article.publish_date, article.summary, (sentiment_text, sentiment_color), validity_status
    else:
        return None, None, None, None, "Failed to fetch article"

st.title("📰  GISTIFY ")

# Text input field with light blue label
url = st.text_input("Enter News Article URL:")

# Center the "Summarize" button
st.markdown(
    """
    <style>
    div.stButton > button {
        display: block;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Summarize"):
    title, pub_date, summary, sentiment, validity = summarize(url)
    
    if title:
        st.subheader("📌 Title")
        st.write(title)
        
        st.subheader("📅 Publication Date")
        st.write(pub_date if pub_date else "Not available")
        
        st.subheader("📖 Summary")
        st.write(summary)
        
        st.subheader("🧠 Sentiment Analysis")
        sentiment_text, sentiment_color = sentiment
        st.markdown(f"<span style='color:{sentiment_color}; font-size:16px;'>{sentiment_text}</span>", unsafe_allow_html=True)
        
        st.subheader("🌐 Website Trustworthiness")
        st.write(validity)
    else:
        st.error("Could not fetch the article. Please check the URL.")