# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크래핑

import urllib.request as req

# 파일 URL
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20141212_111%2Fenactusblog_1418387245204MVk2A_JPEG%2FIMG_1818.JPG&type=sc960_832'
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = 'C:\\test1.jpg'
save_path2 = 'C:\\index.html'

# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print("Download failed")
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))