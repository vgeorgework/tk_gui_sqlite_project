#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import random
import backend as myback # i imported the backend file as an object
from Tkinter import StringVar

root = Tkinter.Tk()
root.configure(bg="white")
root.title("My Super To Do List")
root.geometry("500x500")
print "haiiiiiiiiiiii"

def add_task():
   print "This is the place you need to add the insert comand which is in backend.py",txt_input.get()
   #myback.connect() #accessing connect function from backend.py
   myback.insert(1,txt_input.get())


def del_all():
   pass

def del_one():
   pass



lbl_title=Tkinter.Label(root,text="Reminder",bg="white")
lbl_title.pack()

lbl_display=Tkinter.Label(root,text=" ",bg="white")
lbl_display.pack()


txt_input = Tkinter.Entry(root,width=15)
txt_input.pack()

btn_add_task=Tkinter.Button(root,text="Add task",fg='green',bg='white',command=add_task)
btn_add_task.pack()

btn_del_task=Tkinter.Button(root,text="Delete All",fg='green',bg='white',command=del_all)
btn_del_task.pack()

btn_del_one_task=Tkinter.Button(root,text="Delete One",fg='green',bg='white',command=del_one)
btn_del_one_task.pack()

btn_quit=Tkinter.Button(root,text="Exit",fg='green',bg='white',command=exit)
btn_quit.pack()

lb_tasks=Tkinter.Listbox(root)
lb_tasks.pack()


root.mainloop()
