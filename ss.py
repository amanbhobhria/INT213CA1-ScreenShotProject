import time
from tkinter import *
import pyautogui

def ss():
    name = int(round(time.time() * 1000))
    name = 'Image' + '{}.png'.format(name)

    #time.sleep(1)
    img = pyautogui.screenshot(name)
    img.show()
    root.deiconify()


def delay():
    root.withdraw()
    root.after(1000,ss)

root = Tk()
root.title('Screenshot')
root['bg']= 'black'
root.geometry('300x300')
root.resizable(0,0)
btn1 = Button(root,text='Take Screenshot',font = ('Arial',10,'bold'),height = 2,width =18,fg='Blue',bg='black',command= delay).place(x=45,y=20)
btn2 = Button(root,text = 'Quit',font =('Arial',10,'bold'),height = 2,width =18,fg='Blue',bg='black',command = quit).place(x=45,y=80)

root.mainloop()
exit()
