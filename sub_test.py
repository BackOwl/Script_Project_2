from selenium import webdriver
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
print(S.Now_Url)
#print(len(Web_list))
