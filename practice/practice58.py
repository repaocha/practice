#!/usr/bin/python
# -*- coding:UTF-8 -*-

#��ͼ��ѧ��rectangle������

if __name__=='__main__':
    from Tkinter import *
    root=Tk()
    root.title('Rectangle')
    canvas=Canvas(root,width=400,height=400,bg='blue')
    x0=200
    y0=200
    y1=210
    x1=210
    for i in range(19):
        canvas.create_rectangle(x0,y0,x1,y1)
        x0-=5
        y0-=5
        x1+=5
        y1+=5   
    canvas.pack()
    root.mainloop()