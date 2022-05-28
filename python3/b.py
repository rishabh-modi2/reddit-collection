import requests, time, json
def FetchSubmission():
#    before = 1635485583
    before = 1644736021
    for a in range(1, 1581):
        url = "error found"
        sub = 'Chodi'
        print(str(a))# url = 'https://api.pushshift.io/reddit/search/submission?subreddit=' + sub + '&sort_type=created_utc&size=1000&before=' + str(before)
        # print(url)
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
            rurl = jso['data'][i]['url']
            rid = jso['data'][i]['id']
            rfulllink = jso['data'][i]['full_link']
            rtitle = jso['data'][i]['title']
          except Exception as e:
            print(e)
            pass
          try:
             if ".jpg" in rurl or ".png" in rurl or ".jpeg" in rurl:
#             print(r.json()['data'][i]['score'])
              r2 = requests.get(rurl)
              if r2.status_code != 404:
                wr1 = open(sub + '_' + '_image.txt', 'a+')
                wr1.write(rurl + '\n')  
                wr1 = open(sub + '_image_permalink.txt', 'a+')
                wr1.write(rfulllink + '\n')
                wr1 = open(sub + '_im+perma.txt', 'a+')
                wr1.write(rurl + '\nPermalink: ' + rfulllink + '\nID: ' + rid + '\nFlair: ' + jso['data'][i]['link_flair_text'] + '\n\n')
            # except:
            #   pass
          except Exception as e:
            print(e)
            pass
          try:
              if 'v.red' in rurl:
                r2 = requests.get(rurl)
                if r2.status_code != 404:
                  wr1 = open(sub + '_' + '_video.txt', 'a+')
                  wr1.write(rurl + '\n')  
                  wr1 = open(sub + '_video_permalink.txt', 'a+')
                  wr1.write(rfulllink + '\n')
                  wr1 = open(sub + '_vid+perma.txt', 'a+')
                  wr1.write('Title: ' + rtitle + '\nurl: ' + rurl + '\nPermalink: ' + rfulllink + '\nID: ' + rid + '\nFlair: ' + jso['data'][i]['link_flair_text'] + '\n\n')
          except Exception as e:
            print(e)
            pass
          try:
            if jso['data'][i]['selftext']:
                if jso['data'][i]['selftext'] != '' or jso['data'][i]['selftext'] != '[removed]':
                  wr1 = open(sub + '_' + '_selftext.txt', 'a+')
                  wr1.write(jso['data'][i]['selftext'] + '\n')
                  wr1 = open(sub + '_selftext+perma.txt', 'a+')
                  wr1.write("Title: " + repr(rtitle) + '\n' + "Body: " + repr(jso['data'][i]['selftext']) + '\nPermalink: ' + rfulllink + "\nAuthor: " + repr(jso['data'][i]['author']) + '\n' + "id: " + repr(rid) + "  num_comments: " + repr(jso['data'][i]['num_comments']) + "  score: " + repr(jso['data'][i]['score']) + '\nFlair :' + jso['data'][i]['link_flair_text'] + '\n\n')
          except Exception as e:
            print(e)
            pass
                #print("Title: " + repr(rtitle) + '\n' + "Body " + repr(r.json()['data'][i]['selftext']) + '\n'
            # n = open(sub + 'before.txt', 'a+')
            # n.write(str(before))
#        time.sleep(1)
        try:
          before = jso['data'][99]['created_utc']
        except:
          print(url)
          try:
            before = jso['data'][98]['created_utc']
          except:
            print(url)
            try:
              before = jso['data'][97]['created_utc']
            except:
              print(url)
              try:
                before = jso['data'][96]['created_utc']
              except:
                print(url)
                try:
                  before = jso['data'][95]['created_utc']
                except:
                  before = jso['data'][94]['created_utc']
                  print(url)
FetchSubmission()
