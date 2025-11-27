import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

# Download NLTK data (only first time)
nltk.download('punkt')
nltk.download('stopwords')

def generate_summary(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("english"))
    word_frequencies = {}

    for word in words:
        if word not in stop_words and word not in string.punctuation:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    # Calculate sentence scores
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]

    # Pick top 30% sentences
    select_len = int(len(sentences) * 0.3)
    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:select_len]

    return " ".join(summary)