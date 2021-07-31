# Section06-3
# Selenium
# Selenium 사용 실습(3) - 실습 프로젝트(1)

# selenium 임포트
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import xlsxwriter

#webdriver 설정
browser = webdriver.Chrome('./webdriver/chromedriver.exe')

#크롬 브라우저 내부 대기
browser.implicitly_wait(5)

#브라우저 사이즈
browser.set_window_size(1920,1280)

#페이지 이동
browser.get('http://prod.danawa.com/list/?cate=12210596&logger_kw=ca_main_more')

#제조사별 더 보기 클릭
# Explicitly wait
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#dlMaker_simple > dd > div.spec_opt_view > button.btn_spec_view.btn_view_more'))).click()
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#searchMaker1452'))).click()

time.sleep(2)

#현재 페이지
cur_page = 1
row_cnt = 1
#최대 페이지 확인
#soup = BeautifulSoup(browser.page_source, 'html.parser')
max_page = 6
#print(max_page)

# 엑셀 처리 선언
workbook = xlsxwriter.Workbook('./xlsx_files/crawling_result.xlsx')
worksheet = workbook.add_worksheet()

while(cur_page <= max_page):
    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    #print(soup.prettify())

    #메인 상품 리스트 가져오기
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    #상품 리스트 확인
    #print(pro_list)

    for v in pro_list:
        #임시 출력
        #상품명, 이미지, 가격 출력
        if v.find('div', {'class':'prod_rel_content'}):

            prod_name = v.select_one('p.prod_name > a').text.strip()
            prod_price = v.select_one('div.prod_pricelist > ul > li:first-child > p.price_sect > a > strong').text
            #print(v.select_one('p.prod_name > a').text.strip())
            #print(v.select_one('div.thumb_image > a.thumb_link > img')['src'])
            #print(v.select_one('div.prod_pricelist > ul > li:first-child > p.price_sect > a > strong').text)

            worksheet.write('A{}'.format(row_cnt), prod_name)
            worksheet.write('B{}'.format(row_cnt), prod_price)

            row_cnt += 1

        #페이지 증가
    cur_page += 1
    print('cur_page:{}'.format(cur_page))
    if cur_page > max_page:
        break
    
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()
    time.sleep(3)
    
    #자원 반환
    del soup

#브라우저 종료
browser.close()

#엑셀 파일 닫기
workbook.close()