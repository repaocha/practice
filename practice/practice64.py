#!/usr/bin/python
# -*- coding:UTF-8 -*-

#¿˚”√ellipse∫Õrectangleª≠Õº°£

if __name__=='__main__':
    from Tkinter import *
    canvas=Canvas(width=400,height=600,bg='blue')
    left=20
    right=50
    top=50
    for i in range(15):
        canvas.create_oval(250-right,250-left,250+right,250+left)
        canvas.create_oval(230,250-top,270,250+top)
        canvas.create_rectangle(20-i,20-i,20+5*i,20+5*i)
        right+=5
        left+=5
        top+=5
        
    canvas.pack()
    mainloop()