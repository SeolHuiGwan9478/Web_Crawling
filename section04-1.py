#Section04-1
#Requests
#requests 사용 스크랩핑(1) - Session

import requests

# #세션 활성화
# s = requests.Session()
# r = s.get('https://www.naver.com') #get 방식으로 요청

# # 수신 데이터
# print(r.text)

# #수신 상태 코드
# print('Status Code : {}'.format(r.status_code))

# #확인
# print('Ok? : {}'.format(r.ok))

# #세션 비활성화
# s.close()

#세션 활성화
s = requests.Session()

# 쿠키 return
r1 = s.get('https://httpbin.org/cookies', cookies={'name':'kim1'})
print(r1.text)

# User-Agent
url = 'https://httpbin.org'
headers = {'user-agent':'nice-man_1.0.0_win10_ram16_home_chrome'}

#Header 정보 전송
r3 = s.get(url, headers=headers)
print(r3.text)

#세션 비활성화
s.close()