from untitled1 import Keyword, NewsKeyword, db


def entity_extract(Id, text):
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
        nk = NewsKeyword(news_id=Id, key_id=key.id)
        db.session.add(nk)
        db.session.commit()