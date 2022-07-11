import requests, time, json

def FetchSubmission():
#    before = 1635485583
    le = input('lenth:  ')
    before = 1626020405
    for a in range(1226, 500000):
        url = "error found"
        sub = 'IndiaSpeaks'
        #print(str(a))# url = 'https://api.pushshift.io/reddit/search/submission?subreddit=' + sub + '&sort_type=created_utc&size=1000&before=' + st>        # print(url)
        # r = requests.get(url)
        # data = r.json()
        # with open(str(a) + 'chodi.json', 'w+') as f:
        #     json.dump(data, f, indent = 1)
        file = 'IndiaSpeaks-comment/' + str(a) + sub + '.json'
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
            rparent_id=jso['data'][i]['parent_id']
            rauthor = jso['data'][i]['author']
            rbody = jso['data'][i]['body']
          except Exception as e:
            print(str(e) + '  at a: ' + str(a) + '  i:  ' + str(i))
            pass
          try:
            if rauthor == 'Tasty-Shame-7957' or '❌' in rbody:
             pass
             #dat = {'Author':  rauthor, 'Body': rbody, 'submission_id': rsubid}
             #open('chodi-hindi.txt', 'a+').write(json.dumps(dat) + ',\n')
            if 'Your submission breaks' in rbody or 'bot' in rbody or 'Unfortunately, your post was removed' in rbody or 'Download Link' in rbody or 'I am a bot' in rbody or 'u-RedditSave' in rbody or '[removed]' in rbody or '[deleted]' in rbody:
             #open('chodi-comment.txt', 'a+').write(repr('Author: ' + rauthor + ' Body: ' + rbody + ' submission_id: ' + rsubid) + '\n')
             askk = 2
            else:
             if len(rbody) > int(le):
              body = rbody.replace("\"", "'")
              #print(body)
              #open(str(le) + '_server-chodi-comment.json', 'a+').write('    ' + json.dumps({'Body': body, 'parent_id': rparent_id}) + ',\n')
              print('a: ' + str(a) + '  i:  ' + str(i),end="\r")
              open(str(le) + '_server-' + sub + '-comment.json', 'a+').write('    ' + json.dumps({'Body': body, 'parent_id': rparent_id}) + ',\n')
            #if rauthor == 'Tasty-Shame-7957' or '❌' in rbody:
            # open('chodi-hindi.txt', 'a+').write(repr('Author: ' + rauthor + ' Body: ' + rbody + ' submission_id: ' + rsubid) + '\n')
          except Exception as e:
             print(e)
             pass

FetchSubmission()
