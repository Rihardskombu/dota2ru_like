import json
import time
import numpy as np
import requests
import random
from datetime import datetime

data = '{"login":"adsky","password":"123qwe","silent":false,"remember":true,' \
       '"referer":"https://dota2.ru/"} '
s = requests.Session()


headers = {'content-type': 'application/json',
           'x-requested-with': 'XMLHttpRequest',
           'Content-Length': '115',
           'Connection': 'keep-alive',
           'Host': 'dota2.ru',
           'User-Agent': 'PostmanRuntime/7.29.0',
           'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br'}
url = 'https://dota2.ru/forum/api/user/auth'
r2 = s.get(url, data=data, headers=headers)

print(r2.status_code)
print(r2.reason)
url2 = 'https://dota2.ru/forum/api/forum/setRateOnPost'

f = open("posts.txt", "r").read().split("\n")
existF = open("existinglikedposts.txt", "r")  # .read().split("\n")
existFarray = existF.read().split("\n")
existF.close()

index = 1
for elem in f:
    if np.in1d(elem, existFarray):
        print("post " + elem + " already was liked. skip it")
        continue
    else:
        existinglikedposts = open('existinglikedposts.txt', 'a')
        data2 = '{"pid":' + elem + ',"smileId":972}'  # data2 = '{"pid":26601448,"smileId":972}'
        r3 = s.post(url2, data=data2, headers=headers)

        #url4 = 'https://dota2.ru/forum/posts/' + elem
        #r4 = s.get(url4, headers=headers)
        #print(r4.status_code + "|" + r4.reason)

        existinglikedposts.write(elem + "\n")
        print(r3.status_code)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        print(r3.reason + " post was liked: " + elem)
        time.sleep(random.randint(10, 60))
        existinglikedposts.close()
        index = index + 1
        print("_____-----")
        if index == 14:
            break


