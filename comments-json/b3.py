import requests, time, json

def FetchSubmission():
#    before = 1635485583
    le = input('lenth:  ')
    before = 1626020405
    for a in range(1, 25000):
        url = "error found"
        sub = 'IndiaSpeaks'
        #print(str(a))# url = 'https://api.pushshift.io/reddit/search/submission?subreddit=' + sub + '&sort_type=created_utc&size=1000&before=' + st>        # print(url)
        # r = requests.get(url)
        # data = r.json()
        # with open(str(a) + 'chodi.json', 'w+') as f:
        #     json.dump(data, f, indent = 1)
        file = str(a) + 'IndiaSpeaks.json'
        jso = json.load(open(file))
        for i in range(0, 100):
          try:
            rsubid = jso['data'][i]['link_id']
            rauthor = jso['data'][i]['author']
            rbody = jso['data'][i]['body']
          except Exception as e:
            print(str(e) + '  at a: ' + str(a) + '  i:  ' + str(i))
            pass
          try:
            open('IndiaSpeaks-comment.txt', 'a+').write(repr('Author: ' + rauthor + ' Body: ' + rbody + ' submission_id: ' + rsubid) + '\n')
            if '/redditsave' in rbody or 'Unfortunately, your post was removed' in rbody or 'Download Link' in rbody or 'I am a bot' in rbody or 'u-RedditSave' in rbody or '[removed]' in rbody or '[deleted]' in rbody or "AutoMod" in rauthor:
             #open('chodi-comment.txt', 'a+').write(repr('Author: ' + rauthor + ' Body: ' + rbody + ' submission_id: ' + rsubid) + '\n')
             askk = 2
            else:
             open('server-IndiaSpeaks-comment.json', 'a+').write('    ' + json.dumps({'Body': rbody, 'submission_id': rsubid}) + ',\n')
             if len(rbody) > int(le):
              #body = rbody
              #print(body)
              open(str(le) + '_server-IndiaSpeaks-comment.json', 'a+').write('    ' + json.dumps({'Body': rbody, 'submission_id': rsubid}) + ',\n')
            print('a: ' + str(a) + '  i:  ' + str(i),end="\r")
            #if rauthor == 'Tasty-Shame-7957' or '❌' in rbody:
            # open('chodi-hindi.txt', 'a+').write(repr('Author: ' + rauthor + ' Body: ' + rbody + ' submission_id: ' + rsubid) + '\n')
          except Exception as e:
             print(e)
             pass

FetchSubmission()
