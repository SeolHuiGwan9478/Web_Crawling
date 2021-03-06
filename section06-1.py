#Section 06-1
#Selenium
#Selenium 사용 실습(1) - 설정 및 기본 테스트
# https://sites.google.com/a/chromium.org/chromedriver/downloads

#selenium 임포트
from selenium import webdriver

#webdriver 설정(Chrome, Firefox 등)
browser = webdriver.Chrome('./webdriver/chromedriver.exe')

#속성 확인
#print(dir(browser))

#브라우저 사이즈
browser.set_window_size(1920,1280) #maximize_window() minimize_window()

# 페이지 이동
browser.get('https://www.daum.net')

# 페이지 내용
print('Page Contents : {}'.format(browser.page_source))

#세션 값 출력
print('Session ID : {}'.format(browser.session_id))

#타이틀 출력
print('Title : {}'.format(browser.title))

#현재 URL 출력
print('URL : {}'.format(browser.current_url))

#현재 쿠키 정보 출력
print('Cookies : {}'.format(browser.get_cookies()))

#검색창 input 선택
element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

#검색어 입력
element.send_keys('한국외국어대학교')

#검색(Form submit)
element.submit()

#스크린 샷 저장
browser.save_screenshot('./website_screenshot1.jpg')

#브라우저 종료
browser.quit()