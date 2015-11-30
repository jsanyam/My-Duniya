import feedparser

from urllib2 import urlopen
from bs4 import BeautifulSoup
import psycopg2
from entity_api import entity_extract
from untitled1 import db
from untitled1 import Article


rss = {
    'http://www.firstpost.com/world/feed',
    'http://www.firstpost.com/economy/feed',
    'http://www.firstpost.com/living/feed',
    'http://www.firstpost.com/sports/feed',
    'http://www.firstpost.com/india/feed',
    'http://www.firstpost.com/politics/feed',
    'http://www.firstpost.com/business/feed',
    'http://www.firstpost.com/investing/feed',
    'http://www.firstpost.com/bollywood/feed',
    'http://www.firstpost.com/tech/feed',
    'http://www.firstpost.com/travel/feed'
}


for key in rss:
  #print(key)
  d = feedparser.parse(key)
  for post in d.entries:
    try:
      html=urlopen(post.link)
      bsObj=BeautifulSoup(html,"html.parser")
      title=post.title
      image= bsObj.find("meta",attrs={"property":"og:image"})["content"]
      description=bsObj.find("meta",attrs={"property":"og:description"})["content"]

      pubdate=bsObj.find("meta",attrs={"property":"article:published_time"})["content"]

      full_story=bsObj.find("div",attrs={"class":"fullCont1"}).get_text()

      # print title
      # print image
      # print description
      # print pubdate
      # print full_story

      category = "Firstpost"

      if not db.session.query(Article).filter(Article.title == title).count():
                    article_a = Article(title=title, full_story=full_story, image=image, category=category,
                                        description=description, pubdate=pubdate)
                    db.session.add(article_a)
                    db.session.commit()
                    print article_a.id
                    entity_extract(article_a.id, full_story)

    except psycopg2.IntegrityError:  # as ie:
                # print ie
                print"Caught"
                db.session.rollback()
                # break
                # continue

          # print "\n\n"
    except Exception as e:
        print e
        pass