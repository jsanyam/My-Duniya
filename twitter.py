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