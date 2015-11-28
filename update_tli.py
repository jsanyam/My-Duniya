import urllib2
import re
from bs4 import BeautifulSoup
import psycopg2
from untitled1 import db, Article


def open(str):
    req = urllib2.Request(str, headers={ 'User-Agent': 'Mozilla/5.0' })
    html = urllib2.urlopen(req).read()
    return html

urls = ['http://thelogicalindian.com/category/story-feed/opinion/','http://thelogicalindian.com/category/story-feed/get-inspired/','http://thelogicalindian.com/category/story-feed/awareness/']
for url in urls:
    html = open(url)
    bsObj = BeautifulSoup(html,"html.parser")
    resultset = bsObj.findAll("h3",attrs={"class":"entry-title"})

    for result in resultset:
        try:
            title = result.text
            match = re.search(r'href=[\'"]?([^\'" >]+)', str(result))
            if match:
                html = open(str(match.group(0))[6:])
                bsObj = BeautifulSoup(html,"html.parser")
                description = bsObj.find("meta",attrs={"property":"og:description"})["content"]
                date = bsObj.find("meta",attrs={"property":"article:published_time"})["content"]

                # title
                #print title

                # image
                image = str(bsObj.find("img",attrs={"class":"attachment-regular-featured wp-post-image"})['src']).replace("//","http://www.")

                simpletext = bsObj.find("div",attrs={"class":"entry-content clearfix"}).get_text()
                str1 = str(bsObj.find("div",attrs={"class":"entry-content clearfix"})).replace("//thelogical","www.thelogical").replace("<a href","<img src")
                pos = str1.find("<button")

                 # story html
                html = str1[0:pos]

                # simpletext for keyword generation
                # print simpletext

                # pub_date
                # print date

                # description
                # print description

                # category
                category = "The Logical Indian"



                # print("\n\n\n\n\n\n")

                if not db.session.query(Article).filter(Article.title == title).count():
                    article_a = Article(title=title, full_story=simpletext, image=image, category=category,
                                        description=description, pubdate=date, html=html)
                    db.session.add(article_a)
                    db.session.commit()
                    print article_a.id

        except psycopg2.IntegrityError:  # as ie:
                # print ie
                print"Caught"
                db.session.rollback()
                # break
                # continue

        except Exception as e:
            print e