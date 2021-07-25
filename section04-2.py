#Section04-2
#Requests
#requests 사용 스크랩핑(2) - JSON

import json
import requests

s = requests.Session()

# 100개 JSON 데이터 요청하기
r = s.get('https://httpbin.org/stream/100')

# 수신 확인
print(r.text)

#수신된 데이터 Encoding 방식 확인
print('Encoding : {}'.format(r.encoding))

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    #print(type(line))
    
    #JSON(Dict) 변환 후 타입 확인
    b = json.loads(line) # str -> dict
    print(b)
    print(type(b))