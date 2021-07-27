#Section05-1
#BeautifulSoup
#BeautifulSoup 사용 스크랩핑(1) - 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Doremouse's story</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is h2 area</h2>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">lacie</a>
            <a data-io="link3" href="http://example.com/little" class="sister" id="link3">Title</a>
        </p>
        <p class="story>
            story....
        </p>
    </body>
</html>
"""

# 예제1(BeautifulSoup 기초)
# bs4 초기화
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup', type(soup))
print('prettify', soup.prettify())

#h1 태그 접근
h1 = soup.html.body.h1
print('h1 : ', h1)

# p 태그 접근
p1 = soup.html.body.p
print('p1: ', p1)

# next_sibling 예제
p2 = p1.next_sibling.next_sibling.next_sibling
print('p2 : ',p2)

# 텍스트 출력
print(h1.string)
print(p1.string)

# 예제2(Find, Find_all)
# bs4 초기화

soup2 = BeautifulSoup(html, 'html.parser')

# a 태그 모두 선택
link1 = soup2.find_all("a") #limit = 2 옵션을 걸면 개수 제한 가능

# 타입 확인
# print(type(link1))

# 리스트 요소 확인
print('links', link1)

link2 = soup2.find_all("a", class_='sister') # 그 외에 id='link2', string='Title', string=['Elsie','Title']
print(link2)

for l in link2:
    print(l.string)

# 첫번째 a 태그 가져오기
link3 = soup2.find("a")

print()
print(link3)
print(link3.string)
print(link3.text)

# 다중 조건
link4 = soup2.find('a', {'class': 'sister', 'data-io':'link3'})

print()
print(link4)
print(link4.text)
print(link4.string)

# 태그로 접근 : find, findall
# css 선택자로 접근 : select_one, select
#예제3(select, select_one)

link5 = soup.select_one('p.title > b')
print()
print(link5)
print(link5.text)
print(link5.string)

link6 = soup2.select_one('a#link1')
print()
print(link6)
print(link6.text)
print(link6.string)

#select, select_one 태그 속성 이용해서 찾기
link7 = soup.select_one('a[data-io="link3"]')

print()
print(link7)
print(link7.text)
print(link7.string)

# 선택자에 맞는 전체 선택
link8 = soup.select('p.story > a')
print()
print(link8)

link9 = soup.select('p.story > a:nth-of-type(2)')

print()
print(link9)

link10 = soup.select('p.story')
for t in link10:
    temp = t.find_all("a")

    if temp:
        for v in temp:
            print('>>>>>', v)
        else:
            print('-----', t)