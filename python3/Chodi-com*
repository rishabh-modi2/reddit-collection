import requests, time, json
def FetchSubmission():
#    before = 1635485583
    before = 1644736021
    for a in range(1, 1581):
        url = "error found"
        sub = 'Chodi'
        #print(str(a))# url = 'https://api.pushshift.io/reddit/search/submission?subreddit=' + sub + '&sort_type=created_utc&size=1000&before=' + st>        # print(url)
        # r = requests.get(url)
        # data = r.json()
        # with open(str(a) + 'chodi.json', 'w+') as f:
        #     json.dump(data, f, indent = 1)
        file = str(a) + 'chodi.json'
        jso = json.load(open(file))
        for i in range(0, 100):
          try:
            # rurl = r.json()['data'][i]['url']
            # rid = r.json()['data'][i]['id']
            # rfulllink = r.json()['data'][i]['full_link']
            # rtitle = r.json()['data'][i]['title']
            # rcreated_utc = r.json()['data'][99]['created_utc']
            #rurl = jso['data'][i]['url']
            rsubid = jso['data'][i]['link_id']
            rauthor = jso['data'][i]['author']
            rbody = jso['data'][i]['body']
          except Exception as e:
            print(e)
            pass
          try:
             open('chodi-comment.text', 'a+').write('Author: ' + rauthor + ' Body: ' + rbody + ' submission_id: ' + rsubid + '\n')
             print('a: ' + str(a) + '  i:  ' + str(i),end=" ")
          except:
             print('error')
             pass
