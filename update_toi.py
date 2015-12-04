from urllib2 import urlopen
from bs4 import BeautifulSoup
import feedparser
from entity_api import entity_extract
from untitled1 import Article, db


def upload():
    toi_rss={'http://timesofindia.indiatimes.com/rssfeedstopstories.cms': 'Top stories',
             'http://timesofindia.indiatimes.com/rssfeeds/1221656.cms': 'Most Recent',
             'http://timesofindia.feedsportal.com/c/33039/f/533916/index.rss': 'India',
             'http://timesofindia.feedsportal.com/c/33039/f/533917/index.rss': 'World',
             'http://timesofindia.feedsportal.com/c/33039/f/533919/index.rss':'Business',
             'http://timesofindia.feedsportal.com/c/33039/f/533920/index.rss':'Cricket',
             'http://timesofindia.feedsportal.com/c/33039/f/533921/index.rss':'Sports',
             'http://dynamic.feedsportal.com/c/33039/f/533968/index.rss':'Health',
             'http://timesofindia.feedsportal.com/c/33039/f/533922/index.rss':'Science',
             'http://timesofindia.feedsportal.com/c/33039/f/533925/index.rss':'Environment',
             'http://timesofindia.feedsportal.com/c/33039/f/533923/index.rss':'Technology',
             'http://timesofindia.feedsportal.com/c/33039/f/533924/index.rss':'Education',
             'http://timesofindia.feedsportal.com/c/33039/f/533928/index.rss':'Entertainment',
             'http://timesofindia.indiatimes.com/rssfeeds/2886704.cms':'Lifestyle'
            }


    for key, value in toi_rss.iteritems():
        # print key
        d = feedparser.parse(key)

        category = value
        for post in d.entries:
            try:
                title = post.title

                dated = post.published

                if "photo" in post.link:
                    continue
                if "live" in post.link:
                    continue
                if "videos" in post.link:
                    continue
                if "listshow" in post.link:
                    continue

                html = urlopen(post.link)
                bsObj = BeautifulSoup(html, "html.parser")

                images = bsObj.find("link", attrs={"rel":"image_src"})
                if images is not None:
                    images=images['href']
                story_list=bsObj.find("div", attrs={"class":"content"})
                if story_list is None:
                    story_list=bsObj.find("div", attrs={"class":"Normal"})
                    #print("story was none")
                description=bsObj.find("meta", {'name':'description'})['content']

                #print('title :'+title+"\n")
                # print(post.link)
                # print('category :'+category+"\n")
                # print('description :'+description+"\n")
                # print('full story :'+story_list.get_text()+"\n")
                #
                # print (""+images)
                # print ('pubdate:'+dated)
                # save below variables in db
                save_title=title
                #save_link=post.link
                save_category=category
                save_description=description
                save_full_story=story_list.get_text()
                save_image=images
                save_date=dated
                try:
                    if not db.session.query(Article).filter(Article.title == save_title).count():
                        article_a = Article(title=save_title, full_story=save_full_story, image=save_image, category=save_category,
                        description=save_description, pubdate=save_date)
                        db.session.add(article_a)
                        db.session.commit()
                        print article_a.id
                        entity_extract(article_a.id, save_full_story, 1)

                except Exception as e:#psycopg2.IntegrityError:
                    print"Caught"
                    db.session.rollback()

            except Exception as e:
                print e

