pip install newspaper3k
pip install nltk
pip install textblob

from textblob import TextBlob
import nltk
from newspaper import Article

url = 'https://www.theguardian.com/commentisfree/2018/feb/17/steven-pinker-media-negative-news'
article = Article(url)

article.download() #Downloads the link’s HTML content
article.parse() #Parse the article
nltk.download('punkt')#1 time download of the sentence tokenizer
article.nlp()#  Keyword extraction wrapper

text = article.summary
print(text)

obj = TextBlob(text)

sentiment = obj.sentiment.polarity
print(sentiment)