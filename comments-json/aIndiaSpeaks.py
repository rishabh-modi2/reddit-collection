import requests, time, json
i = 0
def FetchSubmission():
#    before = 1635485583
    before = 1657276544
    for a in range(13361, 1000000):
        sub = 'IndiaSpeaks'
        url = 'https://api.pushshift.io/reddit/search/submission?subreddit=' + sub + '&sort_type=created_utc&size=1000&before=' + str(before)
        print(url + "   filename: " + 'IndiaSpeaks-comment/' + str(a) + sub)
        r = requests.get(url)
        data = r.json()
        with open('new/' + str(a) + sub, 'w+') as f:
            json.dump(data, f, indent = 1)
        wr1 = open('FileFetch.txt', 'a+')
        wr1.write(str(a) + '\n' + url + '\n' + '\n')
        time.sleep(2)
        try:
           for aa in range(0, 99):
              print(data[aa]['created_utc'])
              if data[aa]['created_utc'] == 1655562578:
                  print("1655562578 reached")
                  break
        except Exception as e:
           print(e)
           pass
        try:
            #for aa in range(0, 99):
            #  if data[aa]['created_utc'] == 1655562578:
            #      print("1655562578 reached")
            #      break
            before = r.json()['data'][99]['created_utc']
        except:
        #    continue
            try:
                before = r.json()['data'][98]['created_utc']
            except:
        #        continue
                try:
                    before = r.json()['data'][97]['created_utc']
                except:
        #            continue
                    try:
                        before = r.json()['data'][96]['created_utc']
                    except:
                        try:
                            before = r.json()['data'][94]['created_utc']
                        except:
                            try:
                                before = r.json()['data'][93]['created_utc']
                            except:
                                try:
                                    before = r.json()['data'][92]['created_utc']
                                except:
                                    try:
                                        before = r.json()['data'][91]['created_utc']
                                    except:
                                        try:
                                            before = r.json()['data'][90]['created_utc']
                                        except:
                                            break
FetchSubmission()
