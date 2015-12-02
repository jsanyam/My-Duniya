from untitled1 import Trend, db


def get_json_tweets():
    try:
            import datetime
            import tweepy
            import json
            import ttp
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

                buzz = json.dumps(json_response)
                trend = Trend.query.filter_by(id=1).first()
                trend.buzz = buzz
                db.session.commit()


            p = ttp.Parser()

            def get_all_tweets(screen_name):


                alltweets = []
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)





                new_tweets = api.user_timeline(screen_name = screen_name,count=200)
                alltweets.extend(new_tweets)
                oldest = alltweets[-1].id - 1

                while len(new_tweets) > 0:
                    try:
                        print(screen_name)
                        print "getting tweets before %s" % (oldest)
                        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
                        alltweets.extend(new_tweets)
                        oldest = alltweets[-1].id - 1

                        print "...%s tweets downloaded so far" % (len(alltweets))

                        if ( datetime.datetime.now().timetuple().tm_yday-alltweets[-1].created_at.timetuple().tm_yday)>4:
                            break
                    except:
                        pass



                data=[]
                for tweet in alltweets:
                    if "#ICYMI" not in tweet.text:
                        if  len(p.parse(tweet.text).tags) :
                            url_list=[]
                            for url in tweet.entities['urls']:
                                if 'twitter' in url['expanded_url']:
                                    continue
                                url_list.append(url['expanded_url'])
                            data.append([tweet.created_at,(p.parse(tweet.text).tags),url_list,tweet.text])
                            #print([tweet.created_at,(p.parse(tweet.text).tags),url_list])

                cur_date=datetime.datetime.now()
                for d in data:
                    for hash in d[1]:
                        for url in d[2]:
                            #print d[1]
                            if hash not in handle:
                                handle[hash]=set()
                                handle[hash].add(screen_name)
                            else:
                                handle[hash].add(screen_name)


                            if hash not in trend_setter:
                                #print(hash+"adding with "+url+"\n")
                                trend_setter[hash]=set()
                                trend_setter[hash].add((url,(cur_date-d[0]).total_seconds()//3600))
                            else :
                                #print(hash+"apending with"+ url+"\n")
                                trend_setter[hash].add((url,(cur_date-d[0]).total_seconds()//3600))
                            #print(trend_setter[hash])




                #print(data)



            if __name__ == '__main__':
                 #pass in the username of the account you want to download
                print(datetime.datetime.now().second)
                get_all_tweets("ndtv")

                get_all_tweets("firstpost")
                get_all_tweets("htTweets")
                get_all_tweets("timesofindia")
                get_all_tweets('ibnlive')

                freq_dict={}
                for key, value in trend_setter.iteritems():
                    freq_dict[key]=len(value)



                ranking={}
                for key, value in trend_setter.iteritems():
                    if len(handle[key])>1:
                        sums=0.0
                        for tuple in value:
                            sums+=tuple[1]

                        ranking[key]=(1+0.0)/len(value)+(sums/len(value))/105





                sorted_x = sorted(ranking.items(), key=operator.itemgetter(1))

                # for i,x in enumerate(sorted_x):
                #     print "rank : "+str(i)+ " hashtag : #"+str(x[0])+"  seed: "+str(x[1])+"\n"


                data=[]
                for i,x in enumerate(sorted_x):
                    sorted_urls=sorted(trend_setter[x[0]],key=operator.itemgetter(1))
                    data.append([str(i+1),"#"+str(x[0]),str(x[1]),"   "+str(sorted_urls)])

                count=0
                send=[]
                for d in data:
                    if count<5:
                        send.append(d[1])
                    else:
                        break
                    count=count+1

                return trend_search(send)
    except Exception as e:
        print e
        pass




get_json_tweets()
#print json