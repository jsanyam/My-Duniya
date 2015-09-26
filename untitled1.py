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
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']  #'sqlite:///esoteric.sqlite' #
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

@app.route("/news/", methods=["GET"])
def news():
    return render_template("base.html")

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
                queryset = Article.query.order_by(Article.id.desc()).limit(10)
                # never return the whole set! As it would be very slow
                result = articles_schema.dump(queryset)
                # jsonify serializes our dict into a proper flask response
                return jsonify({"articles": result.data})
            # else:
            #     return jsonify({"msgs:": ["no data"]}), 404
            # #     return render_template('articles.html')

    elif request.method == "POST":# and request.is_xhr:
        #val1 = (request.get_json(force=True))
        #val1 = request.args.get('Name', 0, str)
        val1 = "" + request.form.get('Name')
        val2 = "" + request.form.get('Desc')
        return jsonify({'name': val1, 'desc': val2})
        #return json.dumps({'status': 'OK', 'name': val1, 'desc': val1})




db.create_all()
#db.drop_all()

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
