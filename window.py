from tkinter import *
from subprocess import call
import winsound
from func import stop
import cv2
import mediapipe as mp
import numpy as np

root=Tk()
root.geometry('400x400')
frame = Frame(root)
frame.pack(pady=20,padx=20)

def Open():
    call(["python", "main.py"])

btn=Button(frame,text='Открыть Файл',command=Open)
btn.pack()

root.mainloop()