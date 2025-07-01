
import re
import string
import unicodedata
from nltk.corpus import stopwords


STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
   
    
    text = unicodedata.normalize('NFKD', text)

    text = text.lower()

    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    text = re.sub(r'<.*?>', '', text)

    text = re.sub(r'\d+', '', text)

    text = text.translate(str.maketrans('', '', string.punctuation))

    text = re.sub(r'\s+', ' ', text).strip()


    tokens = text.split()
    tokens = [word for word in tokens if word not in STOPWORDS]
    cleaned = ' '.join(tokens)

    return cleaned
