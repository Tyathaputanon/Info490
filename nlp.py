# -*- coding: utf-8 -*-
"""INFO490NLP

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12y9yfrRXX5JtDYJg-UgsOhJ0P4W8qrGx
"""

import nltk
# nltk.download('punkt')               # sentence tokenizer
# nltk.download('averaged_perceptron_tagger')  # pos tagger
# nltk.download('maxent_ne_chunker')           # NE tagger
# nltk.download('words')

def do_downloads():
  nltk.download('punkt')
  nltk.download('averaged_perceptron_tagger')
  nltk.download('maxent_ne_chunker')           
  nltk.download('words')
  nltk.download('wordnet')
  nltk.download('stopwords') 
  nltk.download('vader_lexicon')

HUCK_URL= "https://raw.githubusercontent.com/NSF-EC/INFO490Assets/master/src/datasets/pg/huckfinn/huck.txt"

def read_remote(url):
    import requests
    with requests.get(url) as response:
      response.encoding = 'utf-8'
      return response.text

def nltk_tokenize_demo(text):
  for sentence in nltk.sent_tokenize(text):
    tokens = nltk.word_tokenize(sentence)
    print(tokens)
    
# demo = "This is a simple sentence. Followed by another!"
# nltk_tokenize_demo(demo)

def nltk_ne_demo(text):
  for sent in nltk.sent_tokenize(text):
    tokens = nltk.word_tokenize(sent)
    tagged = nltk.pos_tag(tokens)
    for chunk in nltk.ne_chunk(tagged):
      print(chunk)

# demo = 'San Francisco considers banning sidewalk delivery robots'
# nltk_ne_demo(demo)
# s1 = 'San Francisco considers banning sidewalk delivery robots'
# s2 = 'In San Francisco, Aunt Polly considers paying sidewalk delivery robots $20.00.'
# nltk_ne_demo(s2)

def nltk_pos_demo(text):
  for sent in nltk.sent_tokenize(text):
    tokens = nltk.word_tokenize(sent)
    tagged = nltk.pos_tag(tokens)
    for t in tagged:
      print(t)

def nltk_find_people_demo(text):
  for sent in nltk.sent_tokenize(text):
    tagged = nltk.pos_tag(nltk.word_tokenize(sent))
    for chunk in nltk.ne_chunk(tagged):
      if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
        name = ' '.join(c[0] for c in chunk)
        print(name)

# s3 = 'In San Francisco, Aunt Polly considers paying sidewalk delivery robots $20.00.'
# nltk_find_people_demo(s3)

#nltk.download('stopwords') 
from nltk.corpus import stopwords

def nltk_stop_word_demo():
  stop_words = stopwords.words('english')
  print("nltk", stop_words)

import collections
from nltk import ngrams

def nltk_ngram_demo(text):
  tokens = text.lower().split()
  grams = ngrams(tokens, 2)
  
  c = collections.Counter(grams)
  print(c.most_common(10))

# text = "We went to a clump of bushes, and Tom made everybody swear to keep the secret, and then showed them a hole in the hill, right in the thickest part of the bushes. "
# nltk_ngram_demo(text)

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def nltk_sentiment_demo():
  sentiment_analyzer = SentimentIntensityAnalyzer()
#   def polarity_scores(doc):
#     return sentiment_analyzer.polarity_scores(doc)
#   doc1 = "INFO 490 is so fun."
#   doc2 = "INFO 490 is so awful."
#   doc3 = "INFO 490 is so fun that I can't wait to take the follow on course!"
#   doc4 = "INFO 490 is so awful that I am glad there's not a follow on course!"

#  print(polarity_scores(doc1)) # most positive
#  print(polarity_scores(doc2)) # most negative
#  print(polarity_scores(doc3)) # mostly positive, neutral
#  print(polarity_scores(doc4)) # mostly negative, a little positive too

# nltk_sentiment_demo()

def nltk_stem_and_lemm_demo():

  words = ["game","gaming","gamed","games","gamer","grows","fairly","nonsensical"]

  ps  = nltk.stem.PorterStemmer()
  sno = nltk.stem.SnowballStemmer('english')
  lan = nltk.stem.lancaster.LancasterStemmer()
 
  for word in words:
    base  = ps.stem(word)
    sbase = sno.stem(word)
    lbase = lan.stem(word)
  
    s = ''
    if (sbase != base):
      s += "(or {})".format(sbase)
    if (lbase != base and lbase != sbase):
      s += "(or {})".format(lbase)
  
    print("{:11s} stems to {:s} {}".format(word, base, s))

def nlkt_wordnet_demo():
  lemma = nltk.stem.WordNetLemmatizer()
  print(lemma.lemmatize('dogs'))

from nltk import FreqDist

def find_characters_nlp(text,topn):
  output=[]
  for sent in nltk.sent_tokenize(text):
    tagged = nltk.pos_tag(nltk.word_tokenize(sent))
    for chunk in nltk.ne_chunk(tagged):
      if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
        output.append(' '.join(c[0] for c in chunk))
        #print(output)
  fdist = FreqDist(output)
  ans = fdist.most_common(topn)
  return (ans)

text = read_remote(HUCK_URL)
topn = find_characters_nlp(text, 50)
#print(topn)