# coding:utf-8
import logging
import os
from flask import Flask, jsonify, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

import feedparser
from urllib2 import urlopen
from bs4 import BeautifulSoup
import sys


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']  # 'sqlite:///esoteric.sqlite'
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=True)
    full_story = db.Column(db.String(10000), nullable=True)

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
        fields = ('id', 'title', 'full_story')


article_schema = ArticleSchema()
# many -> allow for object list dump
articles_schema = ArticleSchema(many=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/news/", methods=["GET", "POST"])
@app.route("/news/<article_id>", methods=["GET"])
def articles(article_id=None):
    if request.method == "GET":
        if article_id:
            # article = Article.query.get(article_id)

            if request.is_xhr:
                article = Article.query.get(article_id)
                if article is None:
                    return jsonify({"msgs": ["the article you're looking for could not be found"]}), 404
                result = article_schema.dump(article)
                return jsonify({'article': result})
            else:
                # if article is None:
                # abort(404)

                return render_template('base.html')
        else:
            if request.is_xhr:
                queryset = Article.query.limit(10)
                # never return the whole set! As it would be very slow
                # print "hello"
                if queryset is None:
                    return jsonify({"msgs": ["the articles you're looking for could not be found"]}), 404
                result = articles_schema.dump(queryset)
                print "you"
                # jsonify serializes our dict into a proper flask response
                return jsonify({"articles": result.data})
            else:
                return render_template('base.html')

    elif request.method == "POST" and request.is_xhr:
        # print "456"
        #val1 = (request.get_json(force=True))
        #val1 = request.args.get('Name', 0, str)
        val1 = "" + request.form.get('Name')
        val2 = "" + request.form.get('Desc')
        #print "123"
        #print val1.Name
        print val2
        return jsonify({'name': val1, 'desc': val2})
        #return json.dumps({'status': 'OK', 'name': val1, 'desc': val1})



# @app.route("/news/post", methods=["POST"])
# def details():
# if request.method == "POST" and request.is_xhr:
#             print "456"
#             #val1 = (request.get_json(force=True))
#             #val1 = request.args.get('Name', 0, str)
#             val1 = str(request.form.get('Name'))
#             #val2 = request.form.get('desc')
#             print "123"
#             #print val1.Name
#             print val1
#             return jsonify({'name': val1})
#             #return json.dumps({'status': 'OK', 'name': val1, 'desc': val1})

# if article_id:
#     article = Article.query.get(article_id)
#
#     if article is None:
#         return jsonify({"msgs": ["the article you're looking for could not be found"]}), 404
#
#     result = article_schema.dump(article)
#     return jsonify({'article': result})
# else:
#     # never return the whole set! As it would be very slow
#     queryset = Article.query.limit(10)
#     result = articles_schema.dump(queryset)
#
#     # jsonify serializes our dict into a proper flask response
#     return jsonify({"articles": result.data})
#

db.create_all()
#db.drop_all()
# # let's populate our database with some data; empty examples are not that cool
# if Article.query.count() == 0:
#     article_a = Article(title='some title', content='some content')
#     article_b = Article(title='other title', content='other content')
#
#     db.session.add(article_a)
#     db.session.add(article_b)
#     db.session.commit()
#
print("####### Times  of India ######## \n")




toi_rss=[

'http://timesofindia.feedsportal.com/c/33039/f/533917/index.rss']

for link in toi_rss:
  d = feedparser.parse(link)
  #print("-----"+d.feed.title+" -------- \n")
#print(post.description+"\n"+post.enclosures[0].href+" \n")
#for ele in d.feed:
# print(ele)
  for post in d.entries:
   #print(post.title + "\n")
   html = urlopen(post.link)
   bsObj = BeautifulSoup(html, "html.parser")
   story_list=bsObj.find("div",{"class":"Normal"})
   str=""
   for story in story_list:
       str = str + story.get_text()+" "

   #print str
   news_a = Article(title=""+post.title, full_story=str)
   db.session.add(news_a)
   #print news_a.title
   db.session.commit()

#print "wohooo"
#a = Article.query.get(1)
#print a

if __name__ == '__main__':
    # we define the debug environment only if running through command
    app.config['SQLALCHEMY_ECHO'] = True
    #app.debug = True
    app.run()


















# '''
# ht_rss=['http://feeds.hindustantimes.com/HT-HomePage-TopStories','http://feeds.hindustantimes.com/HT-Dontmiss',
#
# 'http://feeds.hindustantimes.com/HT-India',
#
# 'http://feeds.hindustantimes.com/HT-World',
#
# 'http://feeds.hindustantimes.com/HT-Business',
#
# 'http://feeds.hindustantimes.com/HT-Comment',
#
# 'http://feeds.hindustantimes.com/HT-Entertainment',
#
# 'http://feeds.hindustantimes.com/HT-Fashion',
#
# 'http://feeds.hindustantimes.com/HT-Sexandrelationships',
#
# 'http://feeds.hindustantimes.com/HT-Entertainment',
#
# 'http://feeds.hindustantimes.com/HT-auto']
#
#
#
#
#
#
#
#
#
#
# print("####### Hindustan Times ######## \n")
#
#
#
#
# for link in ht_rss:
#
#   d = feedparser.parse(link)
#
#   print("-----"+d.feed.title+" -------- \n")
#
# #print(post.description+"\n"+post.enclosures[0].href+" \n")
#
# #for ele in d.feed:
#
# #  print(ele)
#
#   for post in d.entries:
#
#    print(post.title + " \n" )
#
#    html = urlopen(post.link)
#
#    bsObj = BeautifulSoup(html)
#
#    story_list=bsObj.findAll("p")
#
#    for story in story_list:
#
#         print(story.get_text()+"\n")
#
#    print("\n \n \n \n")
# '''
