# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 사용

import urllib.request as req
from urllib.error import URLError, HTTPError

path_url = ['C:/image1.jpg', 'C:/test.html']
target_url = ['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20141212_111%2Fenactusblog_1418387245204MVk2A_JPEG%2FIMG_1818.JPG&type=sc960_832', 'http://google.com']

for i, url in enumerate(target_url):
    try:
        #웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()
        print("---------------------------------------")

        #상태 정보 중간 출력
        print('Header info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))
        print()
        print("---------------------------------------")
        
        with open(path_url[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed.")
        print("HTTPError code : ", e.code)
    except URLError as e:
        print("Download failed.")
        print("URLError Reason : ", e.reason)

    else:
        print()
        print("Download Succeed")
        