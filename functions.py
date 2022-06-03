from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from PIL import ImageTk, ImageColor,Image,ImageDraw,ImageFont
from tkinter import filedialog, messagebox
import tkinter as tk

import random
import os
import Server as S


def _1_GooGle():
    print('구글구글')
    newWindow = tk.Toplevel()
    labelExample = tk.Label(newWindow, text="New Window")
    buttonExample = tk.Button(newWindow, text="New Window button")
    labelExample.pack()
    buttonExample.pack()
    pass

def _2_MultiMap():
    print('맵맵')
    newWindow = tk.Toplevel()
    pass

def _3_TimerAlram():
    print('알람알람')
    newWindow = tk.Toplevel()
    pass

def Make_fight_image(img):
    Result_Image =Image.open(S.image)
    Result_Image = Result_Image.resize((250, 250))

    img = Image.new('RGBA', (len("Please Do your Work.")*7, 30), 'white')
    Result_Image.paste(img, (60, 90))
    draw = ImageDraw.Draw(Result_Image)  # 여기에 그림을 그리겠다 선언
    fontsFolder = 'c:/Windows/Fonts'  # 폰트 로딩
    LhandwFont = ImageFont.truetype(os.path.join(fontsFolder, 'Lhandw.ttf'), 160)  # 폰트기본 설정
    draw.text((70, 100), "Please Do your Work.",fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),Font=LhandwFont)  # 보라색으로 글씨쓰기

    return ImageTk.PhotoImage(Result_Image)


def open_file(event =None):
    f = open('Server_info.txt', 'rt', encoding='UTF8')
    Read_list = []
    for i in f.readlines():
        Read_list.append(i.replace("\n", ""))

    Read_list[5] =filedialog.askopenfilename(title='Select text files',
                            filetype=(("png files(.png)", ".png"),("jpg files(.jpg)", ".jpg"),("bmp files(.bmp)", ".bmp")))

    with open('Server_info.txt', 'w', encoding='UTF8') as f:
        f.write('\n'.join(Read_list))


def Change_Url(event =None):
    # 많은 검색엔진의 Serch들을 가져온다. 10개이상
    # 그 중 랜덤 4개를 꺼내오고, 맞춰서 이미지 다운 링크를 걸어줄것이다.
    # 가능하다면 논문 검색은 4개로 줄여서 따로 버튼에 넣도록 하자.
    pass

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

