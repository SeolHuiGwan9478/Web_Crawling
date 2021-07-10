# Section02-3
# 파이썬 크롤링 기초
# lxml 사용 기초 스크래핑(1)

import requests
import lxml.html

def main():
    '''
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    '''

    # 스크랩핑 대상 URL
    response = requests.get("https://www.naver.com") #Get, Post 두 가지 방식이 있음

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)
    # 결과 출력
    for url in urls:
        #url 출력
        print(url)
        #파일 쓰기
        #생략

def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    root = lxml.html.fromstring(response.content)

    for a in root.cssselect('.thumb_area .thumb_box._NM_NEWSSTAND_THUMB._NM_NEWSSTAND_THUMB_press_valid .popup_wrap a:nth-child(3)'):
        # 링크
        print(a)
        url = a.get('href')
        urls.append(url)
    return urls

if __name__ == "__main__":
    main()