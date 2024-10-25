import re
import nltk
from nltk.corpus import stopwords
from collections import Counter



def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text



def extract_pos_elements(text, pos_filter):
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    return [word for word, tag in pos_tags 
            if tag.startswith(pos_filter) 
            and word not in stop_words]



def get_word_frequencies(words, top_n=10):
    return Counter(words).most_common(top_n)
