import time
import requests

headers = {'content-type': 'application/json',
           'x-requested-with': 'XMLHttpRequest',
           'Content-Length': '115',
           'Connection': 'keep-alive',
           'Host': 'dota2.ru',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
           'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br'}
           
auth_data = '{"login":"vasya123","password":"gorod321","silent":false,"remember":true,' \
       '"referer":"https://dota2.ru/"} '
       
auth_url = 'https://dota2.ru/forum/api/user/auth' #url 1
session = requests.Session()
auth_request = session.get(auth_url, data=auth_data, headers=headers)
time.sleep(3) #let's wait for 3 seconds


# post id sample https://dota2.ru/forum/posts/28324464
# could be found here: https://dota2.ru/forum/members/jabrano.832438/activity/posts/
# for more info on how to get all user posts - see README.md
like_url = 'https://dota2.ru/forum/api/forum/setRateOnPost' #url 2
like_data = '{"pid":' + "28324464" + ',"smileId":972}'
like_request = session.post(like_url, data=like_data, headers=headers)
print(like_request.status_code) # 200 = ok
