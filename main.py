from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import time
import Server as S






'''
browser = webdriver.Chrome()
browser.get(S.url)

browser2= webdriver.Chrome()
browser2.get(S.url2)
browser.refresh()    #다시 불러오기

html =browser.find_element(By.TAG_NAME, 'html') # 열린 브라우저에서 요소html를 찾기
html.send_keys(Keys.PAGE_DOWN) #스크롤이 내려간다!

#끝까지 스크롤하기
src_count = 0
while src_count < len(browser.page_source):
    src_count = len(browser.page_source)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#이들의 가격들 쫙 출력하기
keyword ='신라면'
url = f'https://www.google.com/search?q={keyword}'

soup = BeautifulSoup(browser.page_source, 'lxml')
elms =soup.find_all(class_= re.compile(r'^basicList_title'))
for e in elms:
    title = e.a['title']
    price = e.next_sibling.find(class_=re.compile('^price_num')).string
    print(f'{price} : {title}')
'''

