import tkinter.ttk
from tkinter import *
from tkinter.ttk import *
import re
import time
import Server as S
import Functions as F

def Stop(event =None):
    window.quit()
Command_List = []


window = Tk()
window.title("Script_2 Program")
window.geometry("400x300+500+200")
window.resizable(False, False)


# 버튼
button1 = Button(window,text=" Google_Help ", command=F._1_GooGle, takefocus=False )
button2 = Button(text=" MultiSearch ", command=F._2_MultiMap, takefocus=False )
button3 = Button(text=" Timer_Alram ", command=F._3_TimerAlram, takefocus=False )

button1.place(x=300, y=30)
button2.place(x=300, y=80)
button3.place(x=300, y=130)

# 사진 출력
tk_image = F.Make_fight_image(S.image)
Label(window, image=tk_image).pack(side=LEFT)

# 메뉴
menu = Menu()
menu_file = Menu(menu, tearoff=False)  # True일경우 메뉴분리
menu_url = Menu(menu, tearoff=False)
menu_file.add_command(label='ChangeImage', command=F.open_file, accelerator='Ctrl+o')
menu_url.add_command(label='ChangeUrl', command=F.Change_Url, accelerator='Ctrl+U')

menu.add_cascade(label='File', menu = menu_file )
menu.add_cascade(label='Url', menu = menu_url )

window.config(menu=menu)
# 키 설정
window.bind("<Escape>", Stop)
window.bind("<Control-o>", F.open_file)
window.bind("<Control-u>", F.Change_Url)


window.mainloop()

