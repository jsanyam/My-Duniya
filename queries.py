from untitled1 import Article, db

# article = Article.query.filter_by(id=92).first()
# print article.category
# article.category = 'Musics'
# db.session.commit()

data = Article.query.all()
for article in data:
    print article.category