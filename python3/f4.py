import requests, time, json, praw

reddit = praw.Reddit(
    client_id="sjAd1LOtxmlJWNZ7cuMGWg",
    client_secret="izHyy-ynwCppgsHFJTrkdlLWaJ9TVw",
    user_agent="ris",
    username="Dank_ka_choda-",
    password="rishabh2003",
    ratelimit_seconds=900,
)


score_range = 0
#    before = 1635485583
before = 1644736021
for a in range(1, 160810):
    url = "error found"
    sub = 'SaimanSays'
    #print(str(a))
    # url = 'https://api.pushshift.io/reddit/search/submission?subreddit=' + sub + '&sort_type=created_utc&size=1000&before=' + str(before)
    # print(url)
    # r = requests.get(url)
    # data = r.json()
    # with open(str(a) + 'chodi.json', 'w+') as f:
    #     json.dump(data, f, indent = 1)
    file = str(a) + sub + '.json'
    jso = json.load(open(file))
    wraw1 = open(sub + '_step2.txt', 'a+')
    wraw1.write(str(a) + '\n')
    time.sleep(2)
    for i in range(0, 100):
      try:
       # print('a ' + str(a) + ' i : ' + str(i))
        rfurl = jso['data'][i]['full_link']
        req = requests.get(rfurl + '.json', headers = {'User-agent': 'your bhkot 0.1'})
#        print(req.status_code)
        print('a ' + str(a) + ' i : ' + str(i) + ' status_code ' + str(req.status_code))
        score = req.json()[0]['data']['children'][0]['data']['score']
        removed = req.json()[0]['data']['children'][0]['data']['removed_by_category']
        if score > 10000:
          score_range = 10000
        elif score > 8000:
          score_range = 8000
        elif score > 4000:
          score_range = 4000
        elif score > 2000:
          score_range = 2000
        elif score > 1000:
          score_range = 1000
        elif score > 500:
          score_range = 500
        elif score > 250:
          score_range = 250
        elif score > 100:
          score_range = 100
        elif score < 100:
          score_range = 50        
      except Exception as e:
        print(e)
      score1 = str(score)
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
            wr11 = open(sub + str(score_range) + '_' + '_image.txt', 'a+')
            wr11.write(rurl + '\n')  
            wr12 = open(sub +  str(score_range) + '_image_permalink.txt', 'a+')
            wr12.write(rfulllink + '\n')
            wr13 = open(sub + str(score_range) + '_im+perma.txt', 'a+')
            # if jso['data'][i]['link_flair_text']:
            #   wr1.write('Title: ' + rtitle + 'Imageurl: <a href=' + rurl + '>View</a>\nFlair: ' + jso['data'][i]['link_flair_text'] + '\n\n')
            # else:
            wr13.write('Title: ' + rtitle + 'Imageurl: <a href=' + rurl + '>View</a>\nID: ' + rid + '\nScore:' + score1 + '\n\n')
        # except:
        #   pass
      except Exception as e:
        print(e)
        pass
      try:
          if 'v.red' in rurl:
            r2 = 42 #requests.get(rurl)
            if r2 != 404:
              wr21 = open(sub + str(score_range) + '_' + '_video.txt', 'a+')
              wr21.write(rurl + '\n')  
              wr31 = open(sub + str(score_range) + '_video_permalink.txt', 'a+')
              wr31.write(rfulllink + '\n')
              wr41 = open(sub + str(score_range) + '_vid+perma.txt', 'a+')
              # if jso['data'][i]['link_flair_text']:
              #   wr1.write('Title: ' + rtitle + '\nurl: <a href=https://videoplayer2.rishabh.ml/rvideo/?url=' + rurl + '>Play</a>\nbaseextract: ' + rid + '\nFlair: ' + jso['data'][i]['link_flair_text'] + '\n\n')
              # else:
              wr41.write('Title: ' + rtitle + '\nurl: <a href=https://videoplayer2.rishabh.ml/rvideo/?url=' + rurl + '>Play</a>\nbaseextract: ' + rid + '\nScore:' + score1 + '\n\n')
      except Exception as e:
        print(e)
        pass
      try:
        if removed != None:
          r2 = 23 #requests.get(rurl)
          if r2 != 404:
            wr51 = open('Removed_' + sub + '.txt', 'a+')
            wr51.write(rurl + '\n')  
            wr16 = open('Removed_' + sub + '_permalink.txt', 'a+')
            wr16.write(rfulllink + '\n')
            wr17 = open('Removed_' + sub + '_Combine.txt', 'a+')
            # if jso['data'][i]['link_flair_text']:
          #   wr1.write('Title: ' + rtitle + '\nurl: <a href=' + rurl + '\nbaseextract: ' + rid + '\nFlair: ' + jso['data'][i]['link_flair_text'] + '\n\n')
          # else:
            wr17.write('Title: ' + rtitle + '\nurl: ' + rurl + '\nbaseextract: ' + rid + '\nScore:' + score1 + '\n\n')
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
#FetchSubmission()
