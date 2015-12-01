import feedparser

from urllib2 import urlopen
from bs4 import BeautifulSoup
import psycopg2
from entity_api import entity_extract
from untitled1 import db, Article


rss = {'http://feeds.feedburner.com/TechCrunch/'}


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



      title= post.title

      image= post.media_content[0]["url"]

      html= str(str1.replace(str2,'')).decode("utf-8")

      description=bsObj.find("meta",attrs={"name":"sailthru.description"})["content"]

      # category
      category="TechCrunch"


      # print title
      # print image
      # print date
      # print description
      # print html
      # print cleantext
      # print category


      if not db.session.query(Article).filter(Article.title == title).count():
                    article_a = Article(title=title, full_story=cleantext, image=image, category=category,
                                        description=description, pubdate=date, html=html)
                    db.session.add(article_a)
                    db.session.commit()
                    print article_a.id
                    #entity_extract(article_a.id, cleantext)
    except psycopg2.IntegrityError:  # as ie:
                # print ie
                print"Caught"
                db.session.rollback()
                # break
                # continue


    except Exception as e:
        print e
        pass