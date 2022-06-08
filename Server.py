f = open('Server_info.txt', 'rt', encoding='UTF8')
Read_list =[]
for i in f.readlines():
    Read_list.append(i.replace("\n", ""))

keyword =Read_list[0]
url1 = Read_list[1] # 무조건 google로 고정.
url2 = Read_list[2]
url3 = Read_list[3]
url4 = Read_list[4]
image =Read_list[5]

Goo_Search ='https://www.google.com/'
headers={
    'User-Agent' : 'headers = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
Now_Browser=[]
Now_Url =[]
