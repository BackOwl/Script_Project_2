from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from PIL import ImageTk, ImageColor,Image,ImageDraw,ImageFont
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.ttk as ttk
import random
import os
import re
import requests
import time
import keyboard
import Server as S

import threading
#
keyword =''
eng_keyword =''

newWindow = tk.Tk()
newWindow.title("Script_2 Program")
newWindow.geometry("500x500+0+250")
newWindow.resizable(False, False)


'''browser = webdriver.Chrome()
browser.get(S.Goo_Search)
S.Now_Browser.append(browser)'''

def Get_Keyword(event=None):
    global keyword
    global eng_keyword
    keyword = Search_Entry.get()
    # 영어로 변환. => 영어 구분 부분 만들어야함.
    browser = webdriver.Chrome()
    browser.get(f'https://papago.naver.com/?sk=ko&tk=en&st={keyword}')
    time.sleep(1)
    eng_keyword = browser.find_element(By.CSS_SELECTOR, "div#txtTarget").text

    # 띄어쓰기 변환
    keyword = keyword.replace(" ", "+")
    eng_keyword = eng_keyword.replace(" ", "+")
    print(keyword,"-> ",eng_keyword)
    browser.close()

    Normal_Search()


# 버튼
# 체크박스에 체크할 경우, 논문으로 검색 -> 두개의 논문사이트는 원격으로 설정해야한다.
# 체크박스에 체크할 경우, 영어로 검색가능한 사이트는 영어까지 검색해서 탭으로 띄우도록 한다. 구글같은거
Search_Entry= ''
ignore_Eng = ''
ignore_Non = ''
ignore_Tab = ''

print('맵맵')
newWindow = tk.Toplevel()
newWindow.title("Search_Multi")
newWindow.geometry("400x300+550+250")
newWindow.resizable(False, False)
newWindow['bg'] = '#b2515b'

# 버튼
# 체크박스에 체크할 경우, 논문으로 검색 -> 두개의 논문사이트는 원격으로 설정해야한다.
# 체크박스에 체크할 경우, 영어로 검색가능한 사이트는 영어까지 검색해서 탭으로 띄우도록 한다. 구글같은거
ignore_Eng = tk.IntVar()
ignore_Non = tk.IntVar()
ignore_Tab = tk.IntVar()
Check_Eng = tk.Checkbutton(newWindow,text='영어 Search',bg ='#2e6797', variable=ignore_Eng)
Check_Non = tk.Checkbutton(newWindow,text='논문 Search',bg ='#2e6797',variable=ignore_Non)
Check_Tab = tk.Checkbutton(newWindow,text='탭 활성 검색',bg ='#2e6797', variable=ignore_Tab)
# ignore_Eng.get() 값가져오기, set(1) 체크하기.

Search_Entry = tk.Entry(newWindow,width=30)
Search_Entry.bind('<Return>', Get_Keyword)

Result_Image = Image.open('Logo.png')
Result_Image = Result_Image.resize((300, 130))
Result_Image = ImageTk.PhotoImage(Result_Image)
Label = tk.Label(newWindow, image=Result_Image)
Label.image = Result_Image

# 여기에 Search이미지 하나 넣어서 검색창처럼 만들 것.

Label.place(x=50, y=10)
Search_Entry.place(x=90, y=150)
Check_Eng.place(x=160, y=190)
Check_Non.place(x=160, y=210)
Check_Tab.place(x=160, y=230)

def Normal_Search():
    # 웹들 부르기
    global ignore_Eng
    global ignore_Non
    global ignore_Tab

    # 주소 가져오기
    f = open('Server_info.txt', 'rt', encoding='UTF8')
    Read_list = []
    Web_list = []
    for i in f.readlines():
        Read_list.append(i.replace("\n", ""))

    f = open('Web_info.txt', 'rt', encoding='UTF8')
    for i in f.readlines():
        Web_list.append(i.replace("\n", ""))

    # 숫자로 정해진 주소번호 4개를 0-5 한글, 6-10영어 11-14논문 Read_list에서 꺼내온다.
    # Web_info에서 그 숫자 번째 줄 주소를 가져온다. 논문 뒤에서 두개
    # 논문 체크일 때
    if (ignore_Non.get()):
        for i in range(3):
            S.Now_Url.append(Web_list[11 + i])
        Nonmun_Search()
    # 영어 체크일 때
    else:
        if (ignore_Eng.get()):
            for i in range(4):
                S.Now_Url.append(Web_list[int((Read_list[i + 1])) % 11])
        # 일반 체크없을 때
        else:
            for i in range(4):
                S.Now_Url.append(Web_list[int(Read_list[i + 1]) % 6])
    # 가져온 주소를 검색키워드 keyword로 치환한다.
    for i in range(4):
        if (ignore_Eng.get()):
            if (int((Read_list[i + 1])) > 5):
                S.Now_Url[i] = re.sub('\{keyword\}', f'{eng_keyword}', S.Now_Url[i])
                print(S.Now_Url[i])
            else:
                S.Now_Url[i] = re.sub('\{keyword\}', f'{keyword}', S.Now_Url[i])
        else:
            S.Now_Url[i] = re.sub('\{keyword\}', f'{keyword}', S.Now_Url[i])

    # 각자 탭에서 검색한다. => 창으로도 가능하게 해보자.
    if (ignore_Non.get()):
        Nonmun_Search()
    else:
        if (ignore_Tab.get()):
            browser = webdriver.Chrome()
            browser.get(S.Now_Url[0])
            time.sleep(0.1)
            for i in range(3):
                browser.execute_script(f'window.open("{S.Now_Url[i + 1]}");')
                time.sleep(0.1)
            S.Now_Browser.append(browser)
        # 창일 경우
        else:
            browser = [webdriver.Chrome for x in range(4)]
            state = [0, 0, 600, 600, 400, 0, 0, 400]
            for i in range(4):

                browser[i] = webdriver.Chrome()
                browser[i].set_window_position(state[i], state[i + 4])
                browser[i].set_window_size(600, 400)
                browser[i].get(S.Now_Url[i])
                time.sleep(0.1)
                S.Now_Browser.append(browser[i])
def Nonmun_Search():
    global ignore_Tab
    global ignore_Eng
    global eng_keyword
    eng_keyword = eng_keyword.replace("+", " ")

    Xpath_List = []
    f = open('Xpath_info.txt', 'rt', encoding='UTF8')
    for i in f.readlines():
        Xpath_List.append(i.replace("\n", ""))

    if (ignore_Tab.get()):
        browser = webdriver.Chrome()
        browser.implicitly_wait(2)
        browser.get(S.Now_Url[0])
        #time.sleep(1)
        browser.find_element(By.XPATH, Xpath_List[0]).click()
        #time.sleep(1)
        if (ignore_Eng.get()):
            browser.find_element(By.XPATH, Xpath_List[0]).send_keys(f"{eng_keyword}")
        else:
            browser.find_element(By.XPATH, Xpath_List[0]).send_keys(f"{keyword}")
            #time.sleep(1)
        browser.find_element(By.XPATH, Xpath_List[0]).send_keys(Keys.ENTER)  # 엔터 입력

        for i in range(1, 3):
            browser.execute_script(f'window.open("{S.Now_Url[i]}");')
            time.sleep(1)
            browser.switch_to.window(browser.window_handles[-1])  # 새로 연 탭으로 이동
            browser.find_element(By.XPATH, Xpath_List[i]).click()
            time.sleep(1)
            if (ignore_Eng.get()):
                browser.find_element(By.XPATH, Xpath_List[i]).send_keys(f"{eng_keyword}")
            else:
                browser.find_element(By.XPATH, Xpath_List[i]).send_keys(f"{keyword}")
                #time.sleep(1)
            browser.find_element(By.XPATH, Xpath_List[i + 3]).send_keys(Keys.ENTER)  # 엔터 입력
            #time.sleep(1)

        S.Now_Browser.append(browser)
    # 창일 경우
    else:
        browser = [webdriver.Chrome for x in range(3)]
        state = [0, 0, 600, 600, 400, 0, 0, 400]
        for i in range(3):
            browser[i] = webdriver.Chrome()
            browser[i].set_window_position(state[i], state[i + 4])
            browser[i].set_window_size(600, 400)
            browser[i].get(S.Now_Url[i])
            time.sleep(1)
            browser[i].find_element(By.XPATH, Xpath_List[i]).click()  # 엔터 입력
            time.sleep(1)
            if (ignore_Eng.get()):
                browser[i].find_element(By.XPATH, Xpath_List[i]).send_keys(f"{eng_keyword}")
            else:
                browser[i].find_element(By.XPATH, Xpath_List[i]).send_keys(f"{keyword}")
            time.sleep(1)
            browser[i].find_element(By.XPATH, Xpath_List[i + 3]).send_keys(Keys.ENTER)  # 엔터 입력
            time.sleep(1)
            S.Now_Browser.append(browser[i])


    pass
def Down_Randomimg():
    # 이미지 랜덤추출 함수도 정의해야함.
    pass
def Copy_Url():
    # #5 STRING 강의파일 참고하여 클립보드에 출처를 복사할 수 있도록해야함.
    pass




newWindow.mainloop()



