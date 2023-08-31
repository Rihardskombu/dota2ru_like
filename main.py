import json
import time
import numpy as np
import requests
import random
from datetime import datetime

headers = {'content-type': 'application/json',
           'x-requested-with': 'XMLHttpRequest',
           'Content-Length': '115',
           'Connection': 'keep-alive',
           'Host': 'dota2.ru',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
           'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br'}

auth_data = '{"login":"qq@gmail.com","password":"dabi-dabi-dabi-www","silent":false,"remember":true,' \
            '"referer":"https://dota2.ru/"} '

auth_url = 'https://dota2.ru/forum/api/user/auth'  # url 1
session = requests.Session()
auth_request = session.get(auth_url, data=auth_data, headers=headers)
time.sleep(3)  # let's wait for 3 seconds

unliked_posts_file = open("unliked_posts_file.txt", "r")
unliked_posts_array = unliked_posts_file.read().split("\n")
unliked_posts_file.close()

liked_posts_file = open("liked_posts_file.txt", "r")
liked_posts_array = liked_posts_file.read().split("\n")
liked_posts_file.close()

day_limit_max = 30
day_limit_iterator = 1

for element in unliked_posts_array:
    if day_limit_iterator == (day_limit_max + 1):
        break
    if np.in1d(element, liked_posts_array):
        print("post " + element + "is already liked. skipping the post")
        continue
    else:
        liked_posts_file = open('liked_posts_file.txt', 'a')
        liked_posts_file.write(element + "\n")
        liked_posts_file.close()
        like_url = 'https://dota2.ru/forum/api/forum/setRateOnPost'  # url 2
        like_data = '{"pid":' + element + ',"smileId":972}'
        like_request = session.post(like_url, data=like_data, headers=headers)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        print(like_request.reason + " post was liked: " + element + " status:" + str(like_request.status_code))
        time.sleep(random.randint(30, 60))

        day_limit_iterator += 1
