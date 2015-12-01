# import os
# from flask import Flask, redirect, url_for, render_template, flash
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.login import LoginManager, UserMixin, login_user, logout_user,\
#     current_user
# from pip.utils import logging
# import sys
# from oauth import OAuthSignIn
# import logging
#
#
# app = Flask(__name__)
# app.logger.addHandler(logging.StreamHandler(sys.stdout))
# app.logger.setLevel(logging.ERROR)
# app.config['SECRET_KEY'] = 'top secret!'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' #os.environ['DATABASE_URL'] #
# from untitled1 import app, login_manager, User, db
#
# app.config['OAUTH_CREDENTIALS'] = {
#     'facebook': {
#         'id': '1508201969495385',
#         'secret': '167e0183ff7392c43283e07bd95f5b83'
#     }
# }
# ##app.config['omniauth'] = facebook, secrets.fb_app_id, secrets.fb_app_secret, scope: 'public_profile,email', info_fields: 'email,name'
#
# db = SQLAlchemy(app)
# lm = LoginManager(app)
# lm.login_view = 'index'
#
#
# class User(UserMixin, db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     social_id = db.Column(db.String(64), nullable=False, unique=True)
#     nickname = db.Column(db.String(64), nullable=False)
#     email = db.Column(db.String(64), nullable=True)
#     #friends = db.Column(db.Text(), nullable=True)
#
#
# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))
#
#
# @app.route('/')
# def index():
#     return render_template('')
#
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
#
#
# @app.route('/authorize/<provider>')
# def oauth_authorize(provider):
#     if not current_user.is_anonymous:
#         return redirect(url_for('personal'))
#     oauth = OAuthSignIn.get_provider(provider)
#     return oauth.authorize()
#
#
# @app.route('/callback/<provider>')
# def oauth_callback(provider):
#     if not current_user.is_anonymous:
#         return redirect(url_for('personal'))
#     oauth = OAuthSignIn.get_provider(provider)
#     social_id, username, email = oauth.callback()
#     if social_id is None:
#         flash('Authentication failed.')
#         return redirect(url_for('news'))
#     user = User.query.filter_by(id=social_id).first()
#     if not user:
#         print username
#         user = User(id=social_id, username=username, email=email, general=0)#, friends=friends) #social_id=social_id,
#         db.session.add(user)
#         db.session.commit()
#     login_user(user, True)
#     return redirect(url_for('personal'))
#
# db.create_all()
#
# if __name__ == '__main__':
#     #db.create_all()
#     app.config['SQLALCHEMY_ECHO'] = True
#     #db.drop_all()
#     app.run(debug=False)