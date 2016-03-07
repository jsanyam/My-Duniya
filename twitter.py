def get_keywords_twitter(account):
  import json
  from monkeylearn import MonkeyLearn

  ml = MonkeyLearn('d398a375923123b5ac17b5382cca7ee7f4966dde')
  data = {
    "twitter_user_name": ,
    "twitter_access_token_key": "",
    "twitter_consumer_key": "",
    "twitter_consumer_secret": "",
    "twitter_access_token_secret": ""

  }
  module_id = 'pi_JJ9JrKvk'
  keys=[]
  res = ml.pipelines.run(module_id, data)
  for results in res.result['keywords']:
    for list in  results['keywords']:
      keys.append(list['keyword'])

  return keys

