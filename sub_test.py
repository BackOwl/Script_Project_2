'''from selenium import webdriver
import time
import re
import Server as S
keyword ='dddddddddddd'
eng_keyword ='eeeeeeeeeeee'
check_list = {'Eng':True,'Non':False,'Tab':False}

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
if(check_list['Non']):
    for i in range(4):
        S.Now_Url.append(Web_list[i+11])
# 영어 체크일 때
else:
    if(check_list['Eng']):
        for i in range(4):
            S.Now_Url.append(Web_list[int((Read_list[i + 1])) % 11])
# 일반 체크없을 때
    else:
        for i in range(4):
            S.Now_Url.append(Web_list[int(Read_list[i+1]) % 6])

for i in range(4):
    if (check_list['Eng']):
        if (int((Read_list[i + 1])) > 5):
            S.Now_Url[i] = re.sub('\{keyword\}', f'{eng_keyword}', S.Now_Url[i])
        else:
            S.Now_Url[i] = re.sub('\{keyword\}', f'{keyword}', S.Now_Url[i])
    else:
        S.Now_Url[i] = re.sub('\{keyword\}', f'{keyword}', S.Now_Url[i])

#----------------------------------------------------------
'''


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
import winsound
import datetime
import platform
#
keyword =''
eng_keyword =''

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

stpwatch_counter_num = 66600
stopwatch_running = False
timer_counter_num = 66600
timer_running = False

newWindow = tk.Tk()
newWindow.title("Script_2 Program")
newWindow.geometry("400x300+550+250")
newWindow.resizable(False, False)

def _3_TimerAlram():
    global time_label
    global date_label
    global get_alarm_time_entry
    global alarm_status_label
    global set_alarm_button
    print('알람알람')
    newWindow = tk.Toplevel()
    newWindow.title("Timer_Alram")
    newWindow.geometry("500x250+1000+200")
    newWindow.resizable(False, False)

    # 버튼

    # 도전전
    tabs_control = ttk.Notebook(newWindow)
    clock_tab = tk.Frame(tabs_control)
    alarm_tab = tk.Frame(tabs_control)
    timer_tab = tk.Frame(tabs_control)
    tabs_control.add(clock_tab, text="Clock")
    tabs_control.add(alarm_tab, text="Alarm")
    tabs_control.pack(expand=1, fill="both")
    time_label = tk.Label(clock_tab, font='calibri 40 bold', foreground='black')
    time_label.pack(anchor='center')
    date_label = tk.Label(clock_tab, font='calibri 40 bold', foreground='black')
    date_label.pack(anchor='s')
    get_alarm_time_entry = tk.Entry(alarm_tab, font='calibri 15 bold')
    get_alarm_time_entry.pack(anchor='center')
    alarm_instructions_label = tk.Label(alarm_tab, font='calibri 10 bold',
                                     text="Enter Alarm Time. Eg -> 01:30 PM\n 01 -> Hour\n 30 -> Minutes")
    alarm_instructions_label.pack(anchor='s')
    set_alarm_button = tk.Button(alarm_tab, text="Set Alarm", command=alarm)
    set_alarm_button.pack(anchor='s')
    alarm_status_label = tk.Label(alarm_tab, font='calibri 15 bold')
    alarm_status_label.pack(anchor='s')
    clock()


def clock():
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
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

newWindow.mainloop()