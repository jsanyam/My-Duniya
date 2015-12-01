def get_json_tweets():
    try:
            import datetime
            import tweepy
            import json
            from ttp import ttp
            import operator
            consumer_key = 'orVBG7irMKWuPZVE3EjzVMHmF'
            consumer_secret = 'iuujp0hKDAYNkK60C7FjxnAA7l5cn4z34lNyGiX686l2BvVtOA'
            access_token = '986776236-0S9XqKSH5mtXq9oRxwpy4IbSM6sVnDP63ifbUEKu'
            access_token_secret = 'JkWIrlvCgpomr1hIcntKFMQ1OiAcxuOGuIw3xCDZmJcIq'

            handle={}
            trend_setter={}


            def trend_search(hash_list):
                consumer_key = 'orVBG7irMKWuPZVE3EjzVMHmF'
                consumer_secret = 'iuujp0hKDAYNkK60C7FjxnAA7l5cn4z34lNyGiX686l2BvVtOA'
                access_token = '986776236-0S9XqKSH5mtXq9oRxwpy4IbSM6sVnDP63ifbUEKu'
                access_token_secret = 'JkWIrlvCgpomr1hIcntKFMQ1OiAcxuOGuIw3xCDZmJcIq'
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
                json_response={}
                for hash in hash_list:
                    q=hash+" -RT"
                    print q
                    alltweets=api.search(q,count=5,result_type='recent')
                    allvideos=api.search(hash,count=2,result_type='popular',filter="videos")
                    allnews=api.search(hash,count=3,result_type='news')
                    list=[]
                    for news in allnews:
                        list.append(api.get_oembed(news.id))
                    for video in allvideos:
                        list.append(api.get_oembed(video.id))
                    #print json.dumps(api.get_oembed(allnews[0].id))
                    for tweets in alltweets:
                        list.append(api.get_oembed(tweets.id))

                    json_response[hash]=list

                return json.dumps(json_response)


            p = ttp.Parser()

            def get_all_tweets(screen_name):


                alltweets = []
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
