📊 Sentiment Analysis using Multinomial Naive Bayes
📌 Project Overview

This project implements a Sentiment Analysis model to classify text as Positive or Negative. The workflow involves data preprocessing, feature extraction using TF-IDF, and training a Multinomial Naive Bayes classifier. The goal is to demonstrate an end-to-end NLP pipeline — from raw text to predictions — using Python and scikit-learn.

📂 Dataset

Source: Kaggle / Sentiment Datasets or any CSV file containing text and sentiment labels.

Format:

text → the review or comment.

label → sentiment category (Positive / Negative).

⚙️ Tech Stack

Python 3.x

Pandas, NumPy – Data manipulation

scikit-learn – TF-IDF vectorization & Naive Bayes model

NLTK – Stopword removal, tokenization

Matplotlib / Seaborn – Visualization

🛠 Steps Implemented

Data Loading

Read CSV file into a Pandas DataFrame.

Data Preprocessing

Removed punctuation.

Removed stopwords.

Converted text to lowercase.

Tokenized sentences into words.

Feature Extraction

Used TF-IDF Vectorizer to convert text into numerical feature vectors.

Model Training

Trained a Multinomial Naive Bayes classifier.

Model Evaluation

Evaluated using Accuracy, Confusion Matrix, and Classification Report.

📈 Results

Algorithm: Multinomial Naive Bayes

Feature Extraction: TF-IDF

Achieved 87% accuracy (replace with your result).