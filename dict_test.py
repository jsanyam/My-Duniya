from flask import json
from untitled1 import Article, article_schema

list = []
for i in range(1, 11):
    result = Article.query.filter_by(id=i).first()
    news = article_schema.dump(result)
    list.append(news.data)
print list
# dict["1"] = "hello"
# dict["2"] = "hy"
print json.dumps(list)