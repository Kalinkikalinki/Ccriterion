from tkinter import *
from subprocess import call
import winsound
from func import stop
import cv2
import mediapipe as mp
import numpy as np
import main
root=Tk()
root.geometry('200x100')
frame = Frame(root)
frame.pack(pady=20,padx=20)

def Open():
    call(["python", "main.py"])

btn=Button(frame,text='Open File',command=Open)
btn.pack()

root.mainloop()