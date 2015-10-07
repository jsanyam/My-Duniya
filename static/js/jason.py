from urllib2 import urlopen
from bs4 import BeautifulSoup
import json
from flask import jsonify

html =urlopen('http://prractice.herokuapp.com/news.json')
bsObj = BeautifulSoup(html, "html.parser")
print bsObj