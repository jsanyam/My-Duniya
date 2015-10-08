# coding:utf-8
import logging
import os
from flask import Flask, jsonify, request, render_template, Session, session
from flask.ext.sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

import feedparser
from urllib2 import urlopen
from bs4 import BeautifulSoup
import sys
import psycopg2
# from sqlalchemy.exc import IntegrityError
# from psycopg2._psycopg import IntegrityError

import tweepy

import urllib
import json
import requests
from string import punctuation


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']  #'sqlite:///esoteric.sqlite'  #
db = SQLAlchemy(app)

json_response = {}

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=True, nullable=True)
    full_story = db.Column(db.Text(), nullable=True)
    image = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    pubdate = db.Column(db.String(40), nullable=True)
    #hello
    def __unicode__(self):
        return self.title

    def __repr__(self):
        return u"%s" % self.title


# we use marshmallow Schema to serialize our articles


class ArticleSchema(Schema):
    """
    Article dict serializer
    """
    url = fields.Method("article_url")

    def article_url(self, article):
        return article.url()

    class Meta:
        # which fields should be serialized?
        fields = ('id', 'title', 'full_story', 'image', 'category', 'description', 'pubdate')


article_schema = ArticleSchema()
# many -> allow for object list dump
articles_schema = ArticleSchema(many=True)


@app.route('/')
def main():
    return render_template("basee.html")

@app.route("/news/", methods=["GET"])
def news():
    return render_template("base.html")

@app.route("/tagnews/<category>")
def tag(category):
    return render_template("base1.html")

@app.route("/senti/<category>")
def senti(category):
    new_url='http://prractice.herokuapp.com/' + category
    g=requests.get(new_url)
    data = g.json()
    array = {}
    i = -1

    for item in data['tag']:
        i += 1
        string = item['full_story']
        string = string.lower()
        for p in list(punctuation):
            string = string.replace(p,'')
            string.encode('utf-8')
            string = string.encode('ascii', 'ignore')
        data = urllib.urlencode({"text":string})
        u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
        the_page = u.read()
        j=json.loads(the_page)
        negative = j['probability']['neg']
        positive = j['probability']['pos']
        neutral = j['probability']['neutral']
        if negative > neutral:
            if negative > positive:
                print 'negative'
                array[i] = 'negative'
            else:
                print 'positive'
                array[i] = 'positive'
        else:
            if negative > positive:
                if negative > 0.5:
                    print 'negative'
                    array[i] = 'negative'
                else:
                    print 'neutral'
                    array[i] = 'neutral'
            else:
                if positive > neutral:
                    print 'positive'
                    array[i] = 'positive'
                else:
                    if positive > 0.5:
                        print 'positive'
                        array[i] = 'positive'
                    else:
                        print 'neutral'
                        array[i] = 'neutral'

    return jsonify({'sentiment': array})

@app.route("/news.json/", methods=["GET", "POST"])
@app.route("/news.json/<article_id>", methods=["GET"])
def articles(article_id=None):
    if request.method == "GET":
        if article_id:

            #if request.is_xhr:
                article = Article.query.get(article_id)
                if article is None:
                    return jsonify({"msgs": ["the article you're looking for could not be found"]}), 404
                result = article_schema.dump(article)
                return jsonify({'article': result})
            # else:
            #     # if article is None:
            #     # abort(404)
            #
            # return render_template('articles.html')
        else:
                #if request.is_xhr:
                queryset = Article.query.order_by(Article.id.desc()).limit(50)
                # never return the whole set! As it would be very slow
                result = articles_schema.dump(queryset)
                # jsonify serializes our dict into a proper flask response
                return jsonify({"articles": result.data})
            # else:
            #     return jsonify({"msgs:": ["no data"]}), 404
            # #     return render_template('articles.html')

    # elif request.method == "POST":# and request.is_xhr:
    #     #val1 = (request.get_json(force=True))
    #     #val1 = request.args.get('Name', 0, str)
    #     val1 = "" + request.form.get('Name')
    #     val2 = "" + request.form.get('Desc')
    #     return jsonify({'name': val1, 'desc': val2})
        #return json.dumps({'status': 'OK', 'name': val1, 'desc': val1})


@app.route('/<category>', methods=["GET"])
def tags(category):
    if request.method == 'GET':
        tag = Article.query.filter(Article.category == category).order_by(Article.id.desc()).limit(50)
        if tag is None:
                    return jsonify({"msgs": ["the tag you're looking for could not be found"]}), 404
        result = articles_schema.dump(tag)
        return jsonify({'tag': result.data})


@app.route("/update-db/", methods=["GET", "POST"])
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
                        # print "Hello"
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
                # continue

    return jsonify({"database": ["Updated Database version"]})


@app.route('/trends/<handles>')
def trend_search(handles):
    hash_list = handles.split('_')
    consumer_key = 'orVBG7irMKWuPZVE3EjzVMHmF'
    consumer_secret = 'iuujp0hKDAYNkK60C7FjxnAA7l5cn4z34lNyGiX686l2BvVtOA'
    access_token = '986776236-0S9XqKSH5mtXq9oRxwpy4IbSM6sVnDP63ifbUEKu'
    access_token_secret = 'JkWIrlvCgpomr1hIcntKFMQ1OiAcxuOGuIw3xCDZmJcIq'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    global json_response
    #json_response = {}
    json_response.clear()
    for hash in hash_list:
        q = "#"+hash+" -RT"
        alltweets = api.search(q,count=5)
        list=[]
        for tweets in alltweets:
            list.append(api.get_oembed(tweets.id))

        json_response[hash] = list

    # print json.dumps(json_response)
    return jsonify({"Tweets": ["Updated Trending Tweets"]})


@app.route('/get_tweets')
def trending():
    return jsonify(json_response)


db.create_all()
#db.drop_all()

if __name__ == '__main__':
    # we define the debug environment only if running through command
    app.config['SQLALCHEMY_ECHO'] = True
    #app.debug = True
    app.run(debug=False)






# @app.route("/update-db/", methods=["GET", "POST"])
# def upload():
#     #let's populate our database with some data; empty examples are not that cool
#     #if request.method == 'POST':
#
#         #val1 = request.form.get('initiate')
#         #print val1
#
#         ht_rss={
#         'http://feeds.hindustantimes.com/HT-HomePage-TopStories':"Topstory",
#         # 'http://feeds.hindustantimes.com/HT-Dontmiss':"Dontmiss",
#         # 'http://feeds.hindustantimes.com/HT-India':"India",
#         # 'http://feeds.hindustantimes.com/HT-World':"World",
#         # 'http://feeds.hindustantimes.com/HT-Business':"Buisiness",
#         # 'http://feeds.hindustantimes.com/HT-Comment':"Opinions",
#         # 'http://feeds.hindustantimes.com/HT-Entertainment':"Entertainment",
#         # 'http://feeds.hindustantimes.com/HT-Fashion':"Fashion",
#         # 'http://feeds.hindustantimes.com/HT-Sexandrelationships':"Lifestyle",
#         # 'http://feeds.hindustantimes.com/HT-auto':"Auto"
#         }
#
#         print("####### Hindustan Times ######## \n")
#
#         for key, value in ht_rss.iteritems():
#             #print(key)
#             d = feedparser.parse(key)
#
#             #category = value
#
#             for post in d.entries:
#                 try:
#                     #title = post.title
#                     #description = post.description
#                     print(post.link)
#                     html = urlopen(post.link)
#                     bsObj = BeautifulSoup(html,"html.parser")
#                     story_list = bsObj.findAll("p")
#                     #images = bsObj.find("link", rel="image_src")
#
#                     full_story = ""
#                     for story in story_list:
#                         full_story += story.get_text()
#
#                     #print('title :'+title+"\n")
#                     #print('category :'+category+"\n")
#                     print bsObj.find("link", rel="image_src")
#                     print '\ndesc:'+post.description+"\n"
#                     print('full_story:'+full_story+"\n")
#                     article_a = Article(title=""+post.title, full_story=full_story, category=""+value,
#                                         description=""+post.description)
#                     #print "Hello"
#                     db.session.add(article_a)
#                     db.session.commit()
#                     print article_a.id
#
#                 except:
#                     continue
#
#         return jsonify({"database": ["Updated Database version"]})






# print("####### Hindustan Times ######## \n")
#
#
#
# for key, value in ht_rss.iteritems():
#   print(key)
#   d = feedparser.parse(key)
#
#
#   category=value
#
#   for post in d.entries:
#    try:
#        title=post.title
#        description=post.description
#        print(post.link)
#        html = urlopen(post.link)
#        bsObj = BeautifulSoup(html,"html.parser")
#        story_list=bsObj.findAll("p")
#        images=icon_link = bsObj.find("link", rel="image_src")
#
#        full_story=""
#        for story in story_list:
#             full_story+=story.get_text()+"\n"
#
#        print('title :'+title+"/n"  )
#        print('category :'+category+"\n")
#        print('description :'+description+"\n")
#        print('full story :'+full_story+"\n")
#        print('image :'+images['href'])
#        print("\n \n \n \n")
#    except:
#       continue;




# print("####### Times  of India ######## \n")
#
#
#
#
# toi_rss=[
#
# 'http://timesofindia.feedsportal.com/c/33039/f/533917/index.rss']
#
# for link in toi_rss:
#   d = feedparser.parse(link)
#   #print("-----"+d.feed.title+" -------- \n")
# #print(post.description+"\n"+post.enclosures[0].href+" \n")
# #for ele in d.feed:
# # print(ele)
#   for post in d.entries:
#    #print(post.title + "\n")
#    html = urlopen(post.link)
#    bsObj = BeautifulSoup(html, "html.parser")
#    story_list=bsObj.find("div",{"class":"Normal"})
#    str=""
#    for story in story_list:
#        str = str + story.get_text()+" "
#
#    #print str
#    news_a = Article(title=""+post.title, full_story=str)
#    db.session.add(news_a)
#    #print news_a.title
#    db.session.commit()


#a = Article.query.get(1)
#print a

