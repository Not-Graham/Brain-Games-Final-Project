import numpy
from pprint import pprint
from time import sleep
import nltk
nltk.download('stopwords')
try:
  from Questgen import main
except:
  os.system("pip install git+https://github.com/ramsrigouthamg/Questgen.ai")
  os.system("pip install git+https://github.com/boudinfl/pke.git")
  os.system("python -m nltk.downloader universal_tagset")
  os.system("python -m spacy download en")
  from Questgen import main
file_exists = exists("/content/s2v_reddit_2015_md.tar.gz")
if file_exists != True:
  os.system("wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz")
  os.system("tar -xvf  s2v_reddit_2015_md.tar.gz")
try:
  import wikipedia
except:
  os.system("pip install wikipedia")
  import wikipedia
import requests
from bs4 import BeautifulSoup
import random
newline = '\n'
