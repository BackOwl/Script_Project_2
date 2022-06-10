from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from PIL import ImageTk, ImageColor,Image,ImageDraw,ImageFont
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import tkinter.ttk as ttk

import random
import os
import re
import time
import keyboard
import pyperclip
#import pyautogui
import winsound
import datetime
import platform
import Server as S

Search_Entry= ''
ignore_Eng = ''
ignore_Non = ''
ignore_Tab = ''

time_label =''
date_label =''
get_alarm_time_entry =''
alarm_status_label =''
set_alarm_button =''
timer_get_entry =''
timer_label =''
timer_start =''
timer_stop =''
timer_reset =''

def _1_GooGle():
    print('구글구글')
    newWindow = tk.Toplevel()
    newWindow.title("Search_Google")
    newWindow.geometry("200x350+1100+100")
    newWindow.resizable(False, False)

    # 버튼
    PL_Button =tk.Button(newWindow, command=typo_PL, text="      +      ")
    MN_Button =tk.Button(newWindow, command=typo_MN, text='      -      ')
    WD_Button =tk.Button(newWindow, command=typo_WD, text='    "   "    ')
    Explain_name = tk.Label(newWindow, text="Explain")
    Explain_main = ScrolledText(newWindow,width= 20, height=15,font=('NanumGothic',10))
    Explain_main.insert(tk.END,"-------음?--------------------" ) #설명문 적을 것.
    Explain_main.configure(state='disabled')

    # 구글 열기
    browser = webdriver.Chrome()
    browser.get(S.Goo_Search)
    S.Now_Browser.append(browser)

    # 현재 클립보드 내용을 계속 보여주는 거도 있었으면 좋겠어..
    # 오토로 강의 켜주고 꺼주는거 있었으면 좋겠다 ㅎ
    PL_Button.pack()
    MN_Button.pack()
    WD_Button.pack()
    Explain_name.pack()
    Explain_main.pack()

def _2_MultiMap():
    global Search_Entry
    global ignore_Eng
    global ignore_Non
    global ignore_Tab

    print('맵맵')
    newWindow = tk.Toplevel()
    newWindow.title("Search_Multi")
    newWindow.geometry("400x300+550+250")
    newWindow.resizable(False, False)

    # 버튼
    # 체크박스에 체크할 경우, 논문으로 검색 -> 두개의 논문사이트는 원격으로 설정해야한다.
    # 체크박스에 체크할 경우, 영어로 검색가능한 사이트는 영어까지 검색해서 탭으로 띄우도록 한다. 구글같은거
    ignore_Eng = tk.IntVar()
    ignore_Non = tk.IntVar()
    ignore_Tab = tk.IntVar()
    Check_Eng = tk.Checkbutton(newWindow,text='영어 Search', variable=ignore_Eng)
    Check_Non = tk.Checkbutton(newWindow,text='논문 Search', variable=ignore_Non)
    Check_Tab = tk.Checkbutton(newWindow,text='탭 활성 검색', variable=ignore_Tab)
    # ignore_Eng.get() 값가져오기, set(1) 체크하기.

    Search_Entry = tk.Entry(newWindow,width=30)
    Search_Entry.bind('<Return>', Get_Keyword)

    Result_Image = Image.open(S.image)
    Result_Image = Result_Image.resize((300, 130))
    Result_Image = ImageTk.PhotoImage(Result_Image)
    Label = tk.Label(newWindow, image=Result_Image)
    Label.image = Result_Image
    # 여기에 Search이미지 하나 넣어서 검색창처럼 만들 것.

    Label.place(x=50, y=10)
    Search_Entry.place(x=100, y=150)
    Check_Eng.place(x=170, y=180)
    Check_Non.place(x=170, y=200)
    Check_Tab.place(x=170, y=220)

def _3_TimerAlram():
    global time_label
    global date_label
    global get_alarm_time_entry
    global alarm_status_label
    global set_alarm_button

    print('알람알람')
    newWindow = tk.Toplevel()
    newWindow.title("Timer_Alram")
    newWindow.geometry("500x400+1000+200")
    newWindow.resizable(False, False)

    # 버튼들
    tabs_control = ttk.Notebook(newWindow)
    clock_tab = tk.Frame(tabs_control)
    alarm_tab = tk.Frame(tabs_control)
    time_label = tk.Label(newWindow, font='calibri 40 bold', foreground='black')
    time_label.place(x=110, y=40)
    date_label = tk.Label(newWindow, font='calibri 40 bold', foreground='black')
    date_label.place(x=120, y=100)
    get_alarm_time_entry = tk.Entry(newWindow, font='calibri 15 bold')
    get_alarm_time_entry.place(x=140, y=200)

    alarm_instructions_label = tk.Label(newWindow, font='calibri 10 bold',text="시간을 입력하세요 Ex) 01:30 PM\n 01 -> 시(Hour)\n 30 -> 분(Min)\n")
    alarm_instructions_label.place(x=140, y=240)
    set_alarm_button = tk.Button(newWindow, text="Set 알람", command=alarm)
    set_alarm_button.place(x=320, y=200)
    alarm_status_label = tk.Label(newWindow, font='calibri 15 bold')
    alarm_status_label.place(x=140, y=280)
    clock()

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

def typo_PL():
    # 2. c+p에 이 함수 연결하기(원격함수?)
    Now_Honkey = typo_PL
    pyperclip.copy('PLPL')

    #1. search 값 받아와서 + 넣고 다시 검색로딩하게
    xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    time.sleep(0.1)  ## 0.5초
    element = S.Now_Browser[0].find_element_by_name('q').send_keys("+")
    #S.Now_Browser[0].find_element(By.XPATH, xpath).send_keys(Keys.ENTER)  # 엔터 입력
    time.sleep(0.1)

    #pyautogui.moveTo(200, 400)
    #pyautogui.click()
    S.Now_Browser[0].find_element(By.XPATH, xpath).click()
    print("나 작동중이에요")

def typo_MN():
    Now_Honkey =typo_MN
    pyperclip.copy('MONO')
    xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    time.sleep(0.1)  ## 0.5초
    element = S.Now_Browser[0].find_element_by_name('q').send_keys("-")
    # S.Now_Browser[0].find_element(By.XPATH, xpath).send_keys(Keys.ENTER)  # 엔터 입력
    time.sleep(0.1)

    # pyautogui.moveTo(200, 400)
    # pyautogui.click()
    S.Now_Browser[0].find_element(By.XPATH, xpath).click()

def typo_WD():
    Now_Honkey = typo_WD
    pyperclip.copy('WDWD')

    xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    time.sleep(0.1)  ## 0.5초
    element = S.Now_Browser[0].find_element_by_name('q').send_keys("\" \"")
    # S.Now_Browser[0].find_element(By.XPATH, xpath).send_keys(Keys.ENTER)  # 엔터 입력
    time.sleep(0.1)

    # pyautogui.moveTo(200, 400)
    # pyautogui.click()
    S.Now_Browser[0].find_element(By.XPATH, xpath).click()

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
            S.Now_Url.append(Web_list[11 +i])
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

    # 다시 검색버튼이 눌렸을 때, 기존 창들 다 닫히게 or 안닫히게 체크박스
    pass

def Get_Keyword(event=None):
    global keyword
    global eng_keyword
    global Search_Entry

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

def Nonmun_Search():
    # 추가적인 논문페이지 구현해서 추가로 띄어 같이 넣기. //12-부터
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
        browser.get(S.Now_Url[0])
        time.sleep(1)
        browser.find_element(By.XPATH, Xpath_List[0]).click()
        time.sleep(1)
        if (ignore_Eng.get()):
            browser.find_element(By.XPATH, Xpath_List[0]).send_keys(f"{eng_keyword}")
        else:
            browser.find_element(By.XPATH, Xpath_List[0]).send_keys(f"{keyword}")
            time.sleep(1)
        browser.find_element(By.XPATH, Xpath_List[0]).send_keys(Keys.ENTER)  # 엔터 입력

        for i in range(1,3):
            browser.execute_script(f'window.open("{S.Now_Url[i]}");')
            time.sleep(1)
            browser.switch_to.window(browser.window_handles[-1])  # 새로 연 탭으로 이동
            browser.find_element(By.XPATH, Xpath_List[i]).click()
            time.sleep(1)
            if (ignore_Eng.get()):
                browser.find_element(By.XPATH, Xpath_List[i]).send_keys(f"{eng_keyword}")
            else:
                browser.find_element(By.XPATH, Xpath_List[i]).send_keys(f"{keyword}")
                time.sleep(1)
            browser.find_element(By.XPATH, Xpath_List[i + 3]).send_keys(Keys.ENTER)  # 엔터 입력
            time.sleep(1)

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
            browser[i].find_element(By.XPATH, Xpath_List[i+3]).send_keys(Keys.ENTER)  # 엔터 입력
            time.sleep(1)
            S.Now_Browser.append(browser[i])
def clock():
    date_time = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S/%p")
    date, time1 = date_time.split()
    time2, time3 = time1.split('/')
    hour, minutes, seconds = time2.split(':')
    if int(hour) > 12 and int(hour) < 24:
        time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
    else:
        time = time2 + ' ' + time3
    time_label.config(text=time)
    date_label.config(text=date)
    time_label.after(1000, clock)

def alarm():
    main_time = datetime.datetime.now().strftime("%H:%M %p")
    alarm_time = get_alarm_time_entry.get()
    alarm_time1, alarm_time2 = alarm_time.split(' ')
    alarm_hour, alarm_minutes = alarm_time1.split(':')
    main_time1, main_time2 = main_time.split(' ')
    main_hour1, main_minutes = main_time1.split(':')

    if int(main_hour1) > 12 and int(main_hour1) < 24:
        main_hour = str(int(main_hour1) - 12)
    else:
        main_hour = main_hour1
    if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes) and main_time2 == alarm_time2:
        for i in range(3):
            alarm_status_label.config(text='시간이 끝났습니다!')
            winsound.Beep(500, 100)
        get_alarm_time_entry.config(state='enabled')
        set_alarm_button.config(state='enabled')
        get_alarm_time_entry.delete(0, tk.END)
        alarm_status_label.config(text='')
    else:
        alarm_status_label.config(text='알람 시작!')
        get_alarm_time_entry.config(state='disabled')
        set_alarm_button.config(state='disabled')
    alarm_status_label.after(1000, alarm)

def Down_Randomimg():
    # 이미지 랜덤추출 함수도 정의해야함.
    pass
def Copy_Url():
    # #5 STRING 강의파일 참고하여 클립보드에 출처를 복사할 수 있도록해야함.
    pass

Now_Honkey=typo_PL
keyboard.add_hotkey('control+a',Now_Honkey)

# https://yobbicorgi.tistory.com/30
