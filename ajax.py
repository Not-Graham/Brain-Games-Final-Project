import numpy
from pprint import pprint
import nltk
nltk.download('stopwords')
try:
  from Questgen import main
except:
  !pip install git+https://github.com/ramsrigouthamg/Questgen.ai
  !pip install git+https://github.com/boudinfl/pke.git
  !python -m nltk.downloader universal_tagset
  !python -m spacy download en
  from Questgen import main
file_exists = exists("/content/s2v_reddit_2015_md.tar.gz")
if file_exists != True:
  !wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
  !tar -xvf  s2v_reddit_2015_md.tar.gz
try:
  import wikipedia
except:
  !pip install wikipedia
  import wikipedia
import requests
from bs4 import BeautifulSoup
import random
newline = '\n'

#computational code goes past this point

for x in range(0, 4): 
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    try:
      summary = wikipedia.summary(title)
    except wikipedia.exceptions.DisambiguationError:
      continue
    except wikipedia.exceptions.PageError:
      continue
    length = len(summary)
    if length >= 1000 or length <= 500:
      continue
    print(f"Title of the article: {title}. The article is {length} characters long. {newline}Do you want to be quizzed on it? (Y/N) After 1 pass you will lose points.")
    ans = input("").lower()
    #print("summary type: ", type(summary))
    if ans == "y" or ans == "yes":
        qe = main.BoolQGen()
        payload = {
          "input_text": summary
          }
        pprint("Text/Reading: " + summary)
        output = qe.predict_boolq(payload)
        pprint("Question: " + random.choice(output['Boolean Questions']))
        
        #print("raw output: ", output)
        #print("length of summary :", length)
        #qg = main.QGen()
        #output = qg.predict_mcq(payload)
        #pprint (output)
    
    elif ans == "n" or ans == "no":
        print("Try Again!")
        continue
    elif ans == "e" or ans == "explicit":
        print("Try Again!")
        continue
#30,000 ms(max of 30 seconds to answer)
