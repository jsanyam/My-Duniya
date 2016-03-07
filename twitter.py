def get_keywords_twitter(account):
  import json
  from monkeylearn import MonkeyLearn

  ml = MonkeyLearn('d398a375923123b5ac17b5382cca7ee7f4966dde')
  data = {
    "twitter_user_name": account,
    "twitter_access_token_key": "986776236-0S9XqKSH5mtXq9oRxwpy4IbSM6sVnDP63ifbUEKu",
    "twitter_consumer_key": "orVBG7irMKWuPZVE3EjzVMHmF",
    "twitter_consumer_secret": "iuujp0hKDAYNkK60C7FjxnAA7l5cn4z34lNyGiX686l2BvVtOA",
    "twitter_access_token_secret": "JkWIrlvCgpomr1hIcntKFMQ1OiAcxuOGuIw3xCDZmJcIq"

  }
  module_id = 'pi_JJ9JrKvk'
  keys=[]
  res = ml.pipelines.run(module_id, data)
  for results in res.result['keywords']:
    for list in  results['keywords']:
      keys.append(list['keyword'])

  return keys

#print get_keywords_twitter('ShahRukhKhanFC')


# # BING search API
# @app.route('/<search_type>/<query>')
# def bing_search(query, search_type = 'Web'):#(query, search_type):
#     #search_type: Web, Image, News, Video
#     key= '97VeFEO22dn8nQ9u3zEx7z3QWNlhjcpoRACSnMyaWWg'
#     query = urllib.quote(query)
#     # create credential for authentication
#     #user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
#     credentials = (':%s' % key).encode('base64')[:-1]
#     auth = 'Basic %s' % credentials
#     #Data.ashx
#     url = 'https://api.datamarket.azure.com/Bing/Search/v1/'+search_type+'?Query=%27'+query+'%27&$top=20&$format=json'
#     request = urllib2.Request(url)
#     request.add_header('Authorization', auth)
#     #request.add_header('User-Agent', user_agent)
#     request_opener = urllib2.build_opener()
#     response = request_opener.open(request)
#     response_data = response.read()
#     dict_result = json.loads(response_data)
#     #print(json.dumps(json_result))
#     result_list = dict_result['d']['results']
#     return jsonify({'data': result_list})
#     #return response_data  #not a good view
