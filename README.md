
# 📰 Gestify – News Summarization and Sentiment Analysis Tool

**Gestify** is a user-friendly web application built with Python and Streamlit that simplifies news consumption. By pasting a news article URL, users instantly get a concise summary and sentiment analysis. It saves time and gives quick insight into the emotional tone of the article.

---

## ✨ Features

- 🔗 **News Scraping**: Extracts article content using `newspaper3k`
- ✂️ **Summarization**: NLP-based extractive summarization using NLTK
- 😀 **Sentiment Analysis**: Detects polarity using `TextBlob`
- 💻 **Streamlit UI**: Clean, dark-mode UI with responsive interaction

---

## 📦 Dependencies

This app requires the following Python packages:

- `streamlit`
- `nltk`
- `textblob`
- `newspaper3k`
- `requests`
- `beautifulsoup4`
- `lxml`

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/advaitmandhare/Gestify.git
cd gestify
````

2. **(Optional but recommended) Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

3. **Install required packages**

```bash
pip install streamlit nltk textblob newspaper3k requests beautifulsoup4 lxml
```

4. **Download required NLTK data**

Open a Python shell and run:

```python
import nltk
nltk.download('punkt')
```

---

## 🚀 Running the App

Run the following command in the terminal:

```bash
streamlit run app.py
```

The app will open automatically in your default web browser.

---

## 🗂️ Project Structure

```
gestify/
│
├── app.py                 # Main Streamlit application
└── README.md              # Project documentation (this file)
```

---

## 📎 License

This project is licensed under the MIT License.

---




