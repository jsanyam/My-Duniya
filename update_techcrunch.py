import feedparser

from urllib2 import urlopen
from bs4 import BeautifulSoup


rss={'http://feeds.feedburner.com/TechCrunch/'}


for key in rss:
  print(key)
  d = feedparser.parse(key)
  for post in d.entries:
    try:
      html=urlopen(post.link)
      bsObj=BeautifulSoup(html,"html.parser")
      str1=str(bsObj.find("div",attrs={"class":"article-entry text"}))
      str2=str(bsObj.find("div",attrs={"class":"aside aside-related-articles"}))
      str3=bsObj.findAll("script")
      cleantext=bsObj.find("div",attrs={"class":"article-entry text"}).get_text()
      date=bsObj.find("meta",attrs={ "class":"swiftype","name":"timestamp"})["content"]
      for string in str3:
          str1=str1.replace(str(string),'')



      #title
      print post.title

      #date
      print date

      #html
      print str1.replace(str2,'')

      #image
      print post.media_content[0]["url"]

      #description
      print bsObj.find("meta",attrs={"name":"sailthru.description"})["content"]

      #clean text
      print cleantext

      #category
      print "techcrunch"

      print "\n\n"
    except Exception as e:
        print e
        pass