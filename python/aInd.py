import requests, time, json
i = 0
def FetchSubmission():
#    before = 1635485583
    before = 1604283906
    for a in range(834, 10000):
        sub = 'IndiaSpeaks'
        url = 'https://api.pushshift.io/reddit/search/submission?subreddit=' + sub + '&sort_type=created_utc&size=1000&before=' + str(before)
        print(url)
        r = requests.get(url)
        data = r.json()
        with open(str(a) + sub + '.json', 'w+') as f:
            json.dump(data, f, indent = 1)
        wr1 = open(sub + 'FileFetch.txt', 'a+')
        wr1.write(str(a) + '\n' + url + '\n' + '\n')
        time.sleep(5)
        try:
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
