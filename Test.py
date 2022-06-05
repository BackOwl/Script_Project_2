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
import time
import keyboard
import Server as S


keyword =''
eng_keyword =''

newWindow = tk.Tk()
newWindow.title("Script_2 Program")
newWindow.geometry("400x300+550+250")
newWindow.resizable(False, False)


'''browser = webdriver.Chrome()
browser.get(S.Goo_Search)
S.Now_Browser.append(browser)'''

def Get_Keyword(event=None):
    global keyword
    global eng_keyword
    Keyword = Search_Entry.get()
    #띄어쓰기 변환
    # 영어로 변환.


# 버튼
# 체크박스에 체크할 경우, 논문으로 검색 -> 두개의 논문사이트는 원격으로 설정해야한다.
# 체크박스에 체크할 경우, 영어로 검색가능한 사이트는 영어까지 검색해서 탭으로 띄우도록 한다. 구글같은거
ignore_Eng = tk.IntVar()
ignore_Non = tk.IntVar()
Check_Eng = tk.Checkbutton(text='영어 Search',variable=ignore_Eng)
Check_Non = tk.Checkbutton(text='논문 Search',variable=ignore_Non)
#ignore_Eng.get() 값가져오기, set(1) 체크하기.

Search_Entry = tk.Entry(width = 30)
Search_Entry.bind('<Return>',Get_Keyword)

Result_Image =Image.open(S.image)
Result_Image =Result_Image.resize((300, 150))
Result_Image = ImageTk.PhotoImage(Result_Image)
#여기에 Search이미지 하나 넣어서 검색창처럼 만들 것. 


Search_Entry.place(x=100,y=150)
Check_Eng.place(x=170,y=180)
Check_Non.place(x=170,y=200)
tk.Label(newWindow, image=Result_Image).place(x=50, y=10)

def Normal_Search():
    # 이 아래로는 엔터 작용 후 넘길 함수로 옳길 예정이다.
    # 웹들 부르기
    # 주소 가져오기
    # 숫자로 정해진 주소번호 4개를 Read_list에 꺼내온다.1-4
    ''' f = open('Server_info.txt', 'rt', encoding='UTF8')
        Read_list = []
        for i in f.readlines():
            Read_list.append(i.replace("\n", ""))'''

    # Web_info에서 그 숫자 번째 줄 주소를 가져온다. 논문 뒤에서 두개

    # 가져온 주소를 검색키워드 keyword로 치환한다. -> 입력받을 수 있음. 이떄, 번역기를 돌려서 영어버전 keyword준비.
    # keyword = 'whathappen?' # 띄어쓰기를 + 로 바꿔야함.

    '''  url = Read_list[4]
    url = re.sub('\{keyword\}', f'{keyword}', url)'''

    # 각자 탭에서 검색한다. => 창으로도 가능하게 해보자.
    pass
def Nonmun_Search():
    pass
def Normal_Eng_Search():
    pass
def Down_Randomimg():
    pass


# 이 아래로는 엔터 작용 후 넘길 함수로 옳길 예정이다.
# 웹들 부르기
# 주소 가져오기
# 숫자로 정해진 주소번호 4개를 Read_list에 꺼내온다.1-4
''' f = open('Server_info.txt', 'rt', encoding='UTF8')
    Read_list = []
    for i in f.readlines():
        Read_list.append(i.replace("\n", ""))'''

# Web_info에서 그 숫자 번째 줄 주소를 가져온다. 논문 뒤에서 두개

# 가져온 주소를 검색키워드 keyword로 치환한다. -> 입력받을 수 있음. 이떄, 번역기를 돌려서 영어버전 keyword준비.
# keyword = 'whathappen?' # 띄어쓰기를 + 로 바꿔야함.

'''  url = Read_list[4]
url = re.sub('\{keyword\}', f'{keyword}', url)'''

# 각자 탭에서 검색한다. => 창으로도 가능하게 해보자.
# 이미지 랜덤추출 함수도 정의해야함.
# #5 STRING 강의파일 참고하여 클립보드에 출처를 복사할 수 있도록해야함.











newWindow.mainloop()



