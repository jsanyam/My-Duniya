# coding:utf-8
import os
import urllib2
from flask import Flask, jsonify, request, render_template, Session, session
from flask.ext.sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

from flask import g, flash, redirect, url_for
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user
from flask.ext.bcrypt import check_password_hash
from flask.ext.bcrypt import generate_password_hash

# from pip.utils import logging
from oauth import OAuthSignIn
import logging

from flask.ext.login import UserMixin

import feedparser
from urllib2 import urlopen
from bs4 import BeautifulSoup
import sys

#import psycopg2
# from sqlalchemy.exc import IntegrityError
# from psycopg2._psycopg import IntegrityError
from sqlalchemy import ForeignKey

import urllib
import json
import requests
from string import punctuation

from wtforms import StringField, PasswordField
from flask_wtf import Form
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length
from search_tag import search_to_json
from twitter import get_keywords_twitter


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']  #'sqlite:///esoteric.sqlite' #
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '1508201969495385',
        'secret': '167e0183ff7392c43283e07bd95f5b83'
    }
}

db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(32))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    general = db.Column(db.Integer, default=1)


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), unique=True, nullable=True)
    full_story = db.Column(db.Text(), nullable=True)
    image = db.Column(db.Text(), nullable=True)
    category = db.Column(db.Text(), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    pubdate = db.Column(db.Text(), nullable=True)
    html = db.Column(db.Text(), nullable=True)

    def __unicode__(self):
        return self.title

    def __repr__(self):
        return u"%s" % self.title


class Keyword(db.Model):
    __tablename__ = 'keywords'

    id = db.Column(db.Integer, primary_key=True)
    key_name = db.Column(db.Text(), unique=True, nullable=True)

    def __unicode__(self):
        return self.key_name

    def __repr__(self):
        return u"%s" % self.key_name


class UserKeyword(db.Model):
    __tablename__ = 'user_key'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.BIGINT, ForeignKey("users.id"), nullable=False)
    key_id = db.Column(db.Integer, ForeignKey("keywords.id"), nullable=False)
    priority = db.Column(db.Float, nullable=False)


    def __unicode__(self):
        return self.priority

    def __repr__(self):
        return u"%f" % self.priority


class NewsKeyword(db.Model):
    __tablename__ = 'news_key'

    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer, ForeignKey("articles.id"), nullable=False)
    key_id = db.Column(db.Integer, ForeignKey("keywords.id"), nullable=False)


    def __unicode__(self):
        return self.id

    def __repr__(self):
        return u"%d" % self.id

class Trend(db.Model):
    __tablename__ = 'trend'

    id = db.Column(db.Integer, primary_key=True)
    buzz = db.Column(db.Text(), nullable=True, default=" ")

    def __unicode__(self):
        return self.json

    def __repr__(self):
        return self.json

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
        fields = ('id', 'title', 'full_story', 'image', 'category', 'description', 'pubdate', 'html')


article_schema = ArticleSchema()
# many -> allow for object list dump
articles_schema = ArticleSchema(many=True)

# we use marshmallow Schema to serialize our keywords
class KeywordSchema(Schema):
    """
    keyword dict serializer
    """
    url = fields.Method("keyword_url")

    def keyword_url(self, keys):
        return keys.url()

    class Meta:
        # which fields should be serialized?
        fields = ('id', 'key_name')


# many -> allow for object list dump
keywords_schema = KeywordSchema(many=True)


def email_exists(form, field):
    if User.query.filter_by(email=field.data).count() > 0: #where(User.username == field.data).exists():
        raise ValidationError("User with that email already exists")


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Regexp(r'^[a-zA-Z0-9_]+$',
                        message = "Username should be one word, letters,"
                        "numbers and underscores only")])
    email = StringField('Email', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


@login_manager.user_loader
def user_loader(user_id):
    user = User.query.filter_by(id=user_id)
    if user.count() == 1:
        return user.one()
    return None


@app.route('/register', methods=('GET', 'POST'))
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data)

        if user.count() == 0:
            user = User(username=form.username.data, email=form.email.data, password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            flash('You have registered the email {0}. Please login'.format(form.email.data))
            return redirect(url_for('login'))

        else:
            flash('The username {0} is already in use.  Please try a new email.'.format(form.username.data))

    return render_template('duniyaregister.html', form=form)


@app.route('/login', methods=("GET", "POST"))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data, general=1)   #db.session.query(User).filter(User.email==form.email.data, User.general!=0)
        if user.count() == 0:
            flash("You haven't registered with us yet or registered with facebook")
        else:
            if check_password_hash(user.one().password, form.password.data):
                login_user(user.one())
                flash("You been logged in", "success")

                return redirect(url_for('personal'))
            else:
                flash("Your email or password doesn't match", "error")
    return render_template('duniyalogin.html', form=form)


@app.route('/register_android', methods=('GET', 'POST'))
def register_android():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form.get('username'))
        if user.count() == 0:
            user2 = User.query.filter_by(email=request.form.get('email'))
            if user2.count() == 0:
                user2 = User(username=request.form.get('username'), email=request.form.get('email'), password=generate_password_hash(request.form.get('password')))
                db.session.add(user2)
                db.session.commit()
                return jsonify({'status': 'registered'})
            else:
                return jsonify({'status': 'This email already exists'})

        return jsonify({'status': 'This username already exists'})


@app.route('/login_android', methods=('GET', 'POST'))
def login_android():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get('email'), general=1) # db.session.query(User).filter(User.email==request.form.get('email), User.general!=0)
        if user.count() == 0:
            return jsonify({'validation': "You haven't registered with us yet or registered with facebook"})
        else:
            if check_password_hash(user.one().password, request.form.get('password')):
                return jsonify({'validation': "You have successfully logged in"})
            else:
                return jsonify({'validation': "Your email or password doesn't match"})


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out","success")
    return redirect(url_for('news'))


@app.route('/fb_android', methods=['GET', 'POST'])
def fb_android():
    if request.method == 'POST':
        me = request.get_json(force=True)
        user = User.query.filter_by(id=me['id']).first()
        if not user:
            user = User(id=me['id'], username=me['email'].split('@')[0], email=me['email'], general=0)#, friends=friends) #social_id=social_id,
            db.session.add(user)
            db.session.commit()
            data = ""
            for item in me['likes']['data']:
                # print item
                if 'about' not in item and 'description' not in item:
                    data = data + item['name'] + " "
                elif 'about' not in item:
                    data = data + item['description'] + " "
                elif 'description' not in item:
                    data = data + item['about'] + " "
                else:
                    data = data + item['description'] + item['about'] + " "
            entity_extract(me['id'], data, 0)

            return jsonify({'result': 'successful'})

        return jsonify({'result': 'success'})


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('personal'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('personal'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email, data = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('news'))
    user = User.query.filter_by(id=social_id).first()
    if not user:
        user = User(id=social_id, username=username, email=email, general=0)#, friends=friends) #social_id=social_id,
        db.session.add(user)
        db.session.commit()
        entity_extract(social_id, data, 0)
    login_user(user, True)
    return redirect(url_for('personal'))


# change this
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('personal'))
    else:
        return redirect(url_for('news'))
        # return redirect(url_for('register'))


@app.route("/personal")
def personal():
    if current_user.is_authenticated:  # and (current_user.general == 0 or current_user.general == 2):
        return render_template("personal.html")
    #else:
    #    return render_template("preference.html")  # pref.html


@app.route('/contact')
def contacts():
    if current_user.is_authenticated:
        return render_template("duniyacontactout.html")
    else:
        return render_template("duniyacontact.html")


@app.route("/news", methods=["GET"])
def news():
    if current_user.is_authenticated:
        return render_template("duniyaout.html")
    else:
        return render_template("duniya.html")


# template opening on clicking tiles
@app.route("/tagnews/<category>")
def tag(category):
    if current_user.is_authenticated:
        return render_template("lifestyleout.html")
    else:
        return render_template("lifestyle.html")


@app.route("/tags")
def tags():
    if current_user.is_authenticated:
        return render_template("usertagout.html")
    else:
        return render_template("usertag.html")


#sentiment analysis returns json
@app.route("/senti/<category>")
def senti(category):
    new_url='http://prractice.herokuapp.com/' + category
    g=requests.get(new_url)
    data = g.json()
    array = {}
    #lst = []
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

# REST implementing to return whole news or id wise news in json
@app.route("/news.json/", methods=["GET", "POST"])
@app.route("/news.json/<article_id>", methods=["GET"])
def articles(article_id=None):
    if request.method == "GET":
        if article_id:
            article = Article.query.get(article_id)
            if article is None:
                return jsonify({"msgs": ["the article you're looking for could not be found"]}), 404
            result = article_schema.dump(article)
            return jsonify({'article': result})
        else:
                queryset = Article.query.order_by(Article.id.desc()).limit(50)
                # never return the whole set! As it would be very slow
                result = articles_schema.dump(queryset)
                # jsonify serializes our dict into a proper flask response
                return jsonify({"articles": result.data})

    # elif request.method == "POST":# and request.is_xhr:
    #     #val1 = (request.get_json(force=True))
    #     #val1 = request.args.get('Name', 0, str)
    #     #return json.dumps({'status': 'OK', 'name': val1, 'desc': val1})


# REST implementation to return news category wise
@app.route('/<category>', methods=["GET"])
def tagger(category):
    if request.method == 'GET':
        tag = Article.query.filter(Article.category == category).order_by(Article.id.desc()).limit(50)
        # print tag.category
        if tag is None:
                    return jsonify({"msgs": ["the tag you're looking for could not be found"]}), 404
        result = articles_schema.dump(tag)
        return jsonify({'tag': result.data})


# news with id
@app.route('/full_news/<id>')
def full_news(id):
    if current_user.is_authenticated:
        newsClick(id)
        return render_template("fullnewsout.html")
    else:
        return render_template("fullnews.html")


@app.route('/on_click', methods=['GET', 'POST'])
def on_click():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        uid = user.id
        nk = NewsKeyword.query.filter_by(news_id=request.form.get('newsid')).all()
        for row in nk:
            if not db.session.query(UserKeyword).filter(UserKeyword.key_id == row.key_id, UserKeyword.user_id == uid).count():
                uk = UserKeyword(key_id=row.key_id, user_id=uid, priority=0.1)
                db.session.add(uk)
                db.session.commit()
            else:
                uk = db.session.query(UserKeyword).filter(UserKeyword.key_id == row.key_id, UserKeyword.user_id == uid).first()
                uk.priority += 0.1
                db.session.commit()
        return jsonify({'result': 'success'})

# BING search API
@app.route('/<search_type>/<query>')
def bing_search(query, search_type = 'Web'):#(query, search_type):
    #search_type: Web, Image, News, Video
    key= '97VeFEO22dn8nQ9u3zEx7z3QWNlhjcpoRACSnMyaWWg'
    query = urllib.quote(query)
    # create credential for authentication
    #user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    #Data.ashx
    url = 'https://api.datamarket.azure.com/Bing/Search/v1/'+search_type+'?Query=%27'+query+'%27&$top=20&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    #request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request)
    response_data = response.read()
    dict_result = json.loads(response_data)
    #print(json.dumps(json_result))
    result_list = dict_result['d']['results']
    return jsonify({'data': result_list})
    #return response_data  #not a good view


# URL to update database
@app.route("/update-db/", methods=["GET", "POST"])
def upload():
    toi_rss={'http://timesofindia.indiatimes.com/rssfeedstopstories.cms': 'Top stories',
             'http://timesofindia.indiatimes.com/rssfeeds/1221656.cms': 'Most Recent',
             # 'http://timesofindia.feedsportal.com/c/33039/f/533916/index.rss': 'India',
             # 'http://timesofindia.feedsportal.com/c/33039/f/533917/index.rss': 'World',
             #'http://timesofindia.feedsportal.com/c/33039/f/533919/index.rss':'Business',
             # 'http://timesofindia.feedsportal.com/c/33039/f/533920/index.rss':'Cricket',
             # 'http://timesofindia.feedsportal.com/c/33039/f/533921/index.rss':'Sports',
             # 'http://dynamic.feedsportal.com/c/33039/f/533968/index.rss':'Health',
             # 'http://timesofindia.feedsportal.com/c/33039/f/533922/index.rss':'Science',
             # 'http://timesofindia.feedsportal.com/c/33039/f/533925/index.rss':'Environment',
             # 'http://timesofindia.feedsportal.com/c/33039/f/533923/index.rss':'Technology',
             # 'http://timesofindia.feedsportal.com/c/33039/f/533924/index.rss':'Education',
             # 'http://timesofindia.feedsportal.com/c/33039/f/533928/index.rss':'Entertainment',
             # 'http://timesofindia.indiatimes.com/rssfeeds/2886704.cms':'Lifestyle'
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

                except Exception as e:#psycopg2.IntegrityError:
                    print"Caught"
                    db.session.rollback()

            except Exception as e:
                print e

    return jsonify({"database": ["Updated Database version"]})


@app.route('/trends/')
def trend_search():
    trend = Trend(buzz=" ")
    db.session.add(trend)
    db.session.commit()

@app.route('/get_tweet')
def trendin():
    d={"hello":[1, 2, 3]}
    #return json.dumps(d)
    return jsonify({'d': d})

@app.route('/get_tweets')
def trending():
    trend = Trend.query.filter_by(id=1).first()
    d = json.loads(trend.buzz)
    return jsonify({'tweets': d})


@app.route('/twitter_handle', methods=['GET', 'POST'])
def twitter_handle():
    if request.method == 'POST':
        keys = get_keywords_twitter(request.form.get('account'))
        for key in keys:
            if not db.session.query(Keyword).filter(Keyword.key_name == key).count():
                keyword = Keyword(key_name=key)
                db.session.add(keyword)
                db.session.commit()
            else:
                keyword = Keyword.query.filter_by(key_name=key).first()

            if not UserKeyword.query.filter_by(key_id=keyword.id, user_id=current_user.id).count():  #may not be needed
                uk = UserKeyword(user_id=current_user.id, key_id=keyword.id, priority=1)
                db.session.add(uk)
                db.session.commit()

            else:
                uk = UserKeyword.query.filter_by(key_id=keyword.id, user_id=current_user.id).first()
                uk.priority += 1
                db.session.commit()

        return jsonify({'result': 'updated'})


@app.route('/keywords')
def keywords():
    keys = Keyword.query.order_by(Keyword.id).limit(1000)
    result = keywords_schema.dump(keys)
    return jsonify({'keywords': result.data})


@app.route('/recommended_news', methods=['GET', 'POST'])
def recommended():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        id = user.id
    else:
        id = current_user.id
    dict = {}
    iter = 0
    keys = UserKeyword.query.filter_by(user_id=id).order_by(UserKeyword.priority.desc()).limit(50)
    for key in keys:
        iter += 1
        if iter == 1:
            nk = NewsKeyword.query.filter_by(key_id=key.key_id).order_by(NewsKeyword.news_id.desc()).limit(5)
            if not nk.count():
                iter -= 1
                continue
            list = []
            for data in nk:
                result = Article.query.filter_by(id=data.news_id).first()
                news = article_schema.dump(result)
                list.append(news.data)
            dict["key1"] = list
        elif iter == 2:
            nk = NewsKeyword.query.filter_by(key_id=key.key_id).order_by(NewsKeyword.news_id.desc()).limit(4)
            if not nk.count():
                print "hey"
                iter -= 1
                continue
            list = []
            for data in nk:
                result = Article.query.filter_by(id=data.news_id).first()
                news = article_schema.dump(result)
                list.append(news.data)
            dict["key2"] = list
        elif iter == 3:
            nk = NewsKeyword.query.filter_by(key_id=key.key_id).order_by(NewsKeyword.news_id.desc()).limit(3)
            if not nk.count():
                iter -= 1
                continue
            list = []
            for data in nk:
                result = Article.query.filter_by(id=data.news_id).first()
                news = article_schema.dump(result)
                list.append(news.data)
            dict["key3"] = list
        else:
            nk = NewsKeyword.query.filter_by(key_id=key.key_id).order_by(NewsKeyword.news_id.desc()).limit(2)
            if not nk.count():
                iter -= 1
                continue
            list = []
            for data in nk:
                result = Article.query.filter_by(id=data.news_id).first()
                news = article_schema.dump(result)
                list.append(news.data)
            dict["key"+str(iter)] = list
    return jsonify({'news': dict})


# farji
@app.route('/preference')
def preference():
    return render_template("preferencetry.html")


@app.route('/search_tag', methods=['GET', 'POST'])
def search_tag():
    if request.method == 'POST':
        list =[]
        list = search_to_json(request.form.get('search'))
        return jsonify({'searched': list})


@app.route('/tweet')
def tweet():
    return render_template('personal.html')
   # return render_template('pref.html')


@app.route('/android_receive', methods=['GET', 'POST'])
def android_receive():
    if request.method == 'POST':
        # typo = request.form.get('save')
        # type = request.form.get('desc')
        array = request.get_json(force=True)    # list of keywords
        # print typo
        # print type
        print array[0]
        for keyword in array:
            k = Keyword.query.filter_by(key_name=keyword).first()
            if not UserKeyword.query.filter_by(key_id=k.id, user_id=current_user.id).count():
                uk = UserKeyword(user_id=current_user.id, key_id=k.id, priority=0.5)
                db.session.add(uk)
                db.session.commit()

            else:
                uk = UserKeyword.query.filter_by(key_id=k.id).first()
                uk.priority += 0.5
                db.session.commit()

        return jsonify({'result': 'success'})


@app.route('/receive_keywords', methods=['GET', 'POST'])
def receive_keywords():
    if request.method == 'POST':
        # typo = request.form.get('save')
        # type = request.form.get('desc')
        array = request.form.get('json_str')    # list of keywords
        str= array[1:-1]
        list=str.split(',')
        for l in list:
            print l[1:-1]
        # print typo
        # print type



        # for keyword in array:
        #     k = Keyword.query.filter_by(key_name=keyword).first()
        #     if not UserKeyword.query.filter_by(key_id=k.id, user_id=current_user.id).count():
        #         uk = UserKeyword(user_id=current_user.id, key_id=k.id, priority=0.5)
        #         db.session.add(uk)
        #         db.session.commit()
        #
        #     else:
        #         uk = UserKeyword.query.filter_by(key_id=k.id).first()
        #         uk.priority += 0.5
        #         db.session.commit()

        return jsonify({'result': 'success'})


def entity_extract(Id, text, news):
    from monkeylearn import MonkeyLearn

    ml = MonkeyLearn('f61694907b120433ddc66da1880d537c5f9d8f1e')
    text_list = [text]
    module_id = 'ex_isnnZRbS'
    res = ml.extractors.extract(module_id, text_list)
    for row in res.result[0]:
        if not db.session.query(Keyword).filter(Keyword.key_name == row['entity']).count():
            key = Keyword(key_name=row["entity"])
            db.session.add(key)
            db.session.commit()
        else:
            key = Keyword.query.filter_by(key_name=row["entity"]).first()

        if news:
            nk = NewsKeyword(news_id=Id, key_id=key.id)
            db.session.add(nk)
            db.session.commit()
        else:
            # if not UserKeyword.query.filter_by(key_id=key.id, user_id=Id).count():  #may not be needed
            uk = UserKeyword(user_id=Id, key_id=key.id, priority=1)
            db.session.add(uk)
            db.session.commit()

            # else:
            #     uk = UserKeyword.query.filter_by(key_id=key.id).first()
            #     uk.priority += 1
            #     db.session.commit()


def newsClick(Id):
    nk = NewsKeyword.query.filter_by(news_id=Id).all()
    for row in nk:
        if not db.session.query(UserKeyword).filter(UserKeyword.key_id == row.key_id, UserKeyword.user_id == current_user.id).count():
            uk = UserKeyword(key_id=row.key_id, user_id=current_user.id, priority=0.1)
            db.session.add(uk)
            db.session.commit()
        else:
            uk = db.session.query(UserKeyword).filter(UserKeyword.key_id == row.key_id, UserKeyword.user_id == current_user.id).first()
            uk.priority += 0.1
            db.session.commit()


@app.before_first_request
def init_request():
    db.create_all()

db.create_all()
#db.drop_all()


if __name__ == '__main__':
    # we define the debug environment only if running through command
    app.config['SQLALCHEMY_ECHO'] = True
    app.run(debug=False)



#trend = 'python'
#req = urllib2.Request('http://http://prractice.herokuapp.com/trends/>' + trend)
#response = urllib2.urlopen(req)
#the_page = response.read()
