f = open('Server_info.txt', 'rt', encoding='UTF8')
Read_list =[]
for i in f.readlines():
    Read_list.append(i.replace("\n", ""))

keyword =Read_list[0]
url1 = Read_list[1]
url2 = Read_list[2]
url3 = Read_list[3]
url4 = Read_list[4]

image =Read_list[5]
