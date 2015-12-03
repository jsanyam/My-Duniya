from flask.ext.login import current_user
from untitled1 import NewsKeyword, UserKeyword, db


def newsClick(Id):
    nk = NewsKeyword.query.filter_by(Id).all()
    for row in nk:
        if not db.session.query(UserKeyword).filter(UserKeyword.key_name == row.key_id, UserKeyword.user_id == current_user.id).count():
            uk = UserKeyword(key_id=row.key_id, user_id=current_user.id, priority=0.1)
            db.session.add(uk)
            db.session.commit()
        else:
            uk = db.session.query(UserKeyword).filter(UserKeyword.key_name == row.key_id, UserKeyword.user_id == current_user.id).first()
            uk += 0.1
            db.session.commit()