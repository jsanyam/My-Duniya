import urllib2
from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session


class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('oauth_callback', provider=self.provider_name,
                       _external=True)

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        # print self.providers
        return self.providers[provider_name]


class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')
        self.service = OAuth2Service(
            name='facebook',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://graph.facebook.com/oauth/authorize',
            access_token_url='https://graph.facebook.com/oauth/access_token',
            base_url='https://graph.facebook.com/'
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='email, user_likes, user_birthday, user_hometown',  # user_friends',
            # info_fields='birthday',
            response_type='code',
            redirect_uri=self.get_callback_url())
        )

    def callback(self):  # have to see this function for getting data after login
        if 'code' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(
            data={'code': request.args['code'],
                  'grant_type': 'authorization_code',
                  'redirect_uri': self.get_callback_url()}
        )
        me = oauth_session.get(
            'me?fields=id, name, email, likes.limit(100){name, about, description}').json()    # birthday, picture, hometown, , education

        data = ""
        for item in me['likes']['data']: #['category'])
            # print item
            if 'about' not in item and 'description' not in item:
                data = data + item['name'] + " "
            elif 'about' not in item:
                data = data + item['description'] + " "
            elif 'description' not in item:
                data = data + item['about'] + " "
            else:
                data = data + item['description'] + item['about'] + " "

        return (
            #'facebook$' +
            me['id'],
            # Facebook does not provide username, so the email's username is used instead
            me['email'].split('@')[0],
            me['email'],
            data
        )


# keyword extractor taxonomy classifier about category description name posts(message)