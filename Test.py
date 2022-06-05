from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from PIL import ImageTk, ImageColor,Image,ImageDraw,ImageFont
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
import random
import os
import re
import time
import keyboard
import Server as S

window = Tk()
window.title("Script_2 Program")
window.geometry("400x300+500+200")
window.resizable(False, False)


browser = webdriver.Chrome()
browser.get(S.Goo_Search)
S.Now_Browser.append(browser)
browser.refresh()    #다시 불러오기

#html =browser.find_element(By.TAG_NAME, 'html') # 열린 브라우저에서 요소html를 찾기
#html.send_keys(Keys.PAGE_DOWN) #스크롤이 내려간다!

def why():
    xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    S.Now_Browser[0].find_element(By.XPATH, xpath).click()  # 찾아진 위치에 대해 클릭하기
    time.sleep(0.2)
    keyboard.write('야 너 왜안됌?')

    S.Now_Browser[0].find_element(By.XPATH, xpath).send_keys(Keys.ENTER)  # 엔터 입력

keyboard.add_hotkey('control+a',why)

window.mainloop()
'''#끝까지 스크롤하기
src_count = 0
while src_count < len(browser.page_source):
    src_count = len(browser.page_source)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)'''

'''#이들의 가격들 쫙 출력하기
keyword ='신라면'
url = f'https://www.google.com/search?q={keyword}'

soup = BeautifulSoup(browser.page_source, 'lxml')
elms =soup.find_all(class_= re.compile(r'^basicList_title'))
for e in elms:
    title = e.a['title']
    price = e.next_sibling.find(class_=re.compile('^price_num')).string
    print(f'{price} : {title}')
'''

