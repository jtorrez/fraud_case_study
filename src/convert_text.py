from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
import scipy
from scipy import sparse
from HTMLParser import HTMLParser



def convert_text(texts):
    documents = []
    for text in texts:
        documents.append(text)
    return documents

def convert_table(documents):

    docs = [word_tokenize(content) for content in documents]

    stop = set(stopwords.words('english'))
    docs = [[word for word in words if word not in stop] for words in docs]

    porter = PorterStemmer()
    docs_porter = [[porter.stem(word) for word in words] for words in docs]

    tfidf = TfidfVectorizer(stop_words='english')
    tfidfed = tfidf.fit_transform(documents)

    table = np.hstack(tfidfed)  # a numpy array consisting of 1 x #words sparse matrix

    return table

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def convert_html(html):
    texts = []
    for text in html:
        striped = strip_tags(text.encode('ascii', 'ignore').replace('\r\n', ''))
        texts.append(striped)
    return texts

def html_table(name, description):
    docs = convert_text(name)
    names = convert_table(docs)

    html = convert_html(description)
    descriptions = convert_table(html)

    return np.concatenate((names, descriptions), axis=1)
